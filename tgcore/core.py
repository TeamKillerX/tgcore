# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

"""
Github Author: https://github.com/TeamKillerX/
Code: @zxyeor

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
"""

from __future__ import annotations

import base64
import json
import mimetypes
import os
import re
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import (
    Any,
    BinaryIO,
    Callable,
    Dict,
    Generic,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import httpx
from box import Box

T = TypeVar("T")

FileTuple = Union[
    Tuple[str, Any],
    Tuple[str, Any, str],
]

_PATH_PARAM_RE = re.compile(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}")
MediaType = Literal["photo", "video", "animation", "document"]

def _extract_path_param_keys(path: str) -> list[str]:
    return _PATH_PARAM_RE.findall(path)

def _format_path_and_pop_params(path: str, params: Dict[str, Any]) -> str:
    keys = _extract_path_param_keys(path)
    for k in keys:
        if k not in params:
            raise ValueError(f"Missing path param: {k} for path {path}")
        path = path.replace("{" + k + "}", str(params[k]))
        params.pop(k, None)
    return path

def _is_file_like(x: Any) -> bool:
    return hasattr(x, "read") and callable(x.read)

def _is_uploadfile(x: Any) -> bool:
    return hasattr(x, "filename") and (hasattr(x, "file") or hasattr(x, "read"))

def _guess_content_type(filename: str) -> Optional[str]:
    ctype, _ = mimetypes.guess_type(filename)
    return ctype

def _normalize_tuple_file(v: FileTuple, key: str) -> FileTuple:
    if len(v) not in (2, 3):
        raise ValueError(f"Invalid file tuple length for '{key}': {len(v)}")

    filename = v[0] or f"{key}.bin"
    content = v[1]

    if len(v) == 2:
        ctype = _guess_content_type(filename)
        return (filename, content, ctype) if ctype else (filename, content)

    # len == 3
    ctype = v[2]
    return (filename, content, ctype)

def _try_path_to_file_tuple(path: Union[str, Path], key: str) -> Optional[FileTuple]:
    p = Path(path)
    if not p.exists() or not p.is_file():
        return None

    filename = p.name or f"{key}.bin"
    ctype = _guess_content_type(filename) or "application/octet-stream"
    f = p.open("rb")
    return (filename, f, ctype)

def _bytes_to_file_tuple(data: Union[bytes, bytearray, memoryview], key: str, filename: Optional[str] = None) -> FileTuple:
    b = bytes(data) if not isinstance(data, (bytes,)) else data
    fname = filename or f"{key}.bin"
    ctype = _guess_content_type(fname) or "application/octet-stream"
    return (fname, b, ctype)

def _normalize_form_data(payload: Dict[str, Any]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for k, v in payload.items():
        if v is None:
            continue
        if isinstance(v, (dict, list)):
            out[k] = json.dumps(v, ensure_ascii=False)
        elif isinstance(v, bool):
            out[k] = "true" if v else "false"
        else:
            out[k] = str(v)
    return out

def _extract_files(payload: Dict[str, Any]) -> Dict[str, Any]:
    files: Dict[str, Any] = {}
    to_pop: list[str] = []

    for k, v in list(payload.items()):
        if v is None:
            continue

        if isinstance(v, tuple):
            try:
                norm = _normalize_tuple_file(v, k)  # type: ignore[arg-type]
            except Exception:
                continue

            content = norm[1]
            if _is_file_like(content) or isinstance(content, (bytes, bytearray, memoryview)):
                files[k] = norm
                to_pop.append(k)
            continue

        if _is_uploadfile(v):
            fileobj = getattr(v, "file", None)
            filename = getattr(v, "filename", None) or f"{k}.bin"
            ctype = _guess_content_type(filename) or "application/octet-stream"

            if fileobj is not None and _is_file_like(fileobj):
                files[k] = (filename, fileobj, ctype)
                to_pop.append(k)
                continue

            raise TypeError(
                f"UploadFile '{k}' must provide a sync .file handle, "
                f"or read it to bytes before calling _post."
            )

        if _is_file_like(v):
            filename = getattr(v, "name", None)
            filename = os.path.basename(filename) if isinstance(filename, str) else None
            filename = filename or f"{k}.bin"
            ctype = _guess_content_type(filename) or "application/octet-stream"
            files[k] = (filename, v, ctype)
            to_pop.append(k)
            continue

        if isinstance(v, (bytes, bytearray, memoryview)):
            files[k] = _bytes_to_file_tuple(v, k)
            to_pop.append(k)
            continue

        if isinstance(v, (str, Path)):
            maybe = _try_path_to_file_tuple(v, k)
            if maybe is not None:
                files[k] = maybe
                to_pop.append(k)
            continue

    for k in to_pop:
        payload.pop(k, None)

    return files

class InputMedia:
    def __init__(self, client, type_, media):
        self._client = client
        self._data = {
            "type": type_,
            "media": media
        }

    def caption(self, text: str):
        self._data["caption"] = text
        return self

    def parse_mode(self, mode: str):
        self._data["parse_mode"] = mode
        return self

    def build(self):
        return self._data

class ChatPermissionsBuilder:
    def __init__(self):
        self._data = {}

    def __getattr__(self, name):
        if name.startswith("can_"):
            def setter(value: bool):
                self._data[name] = value
                return self
            return setter
        raise AttributeError(name)

    def build(self):
        return self._data

class MediaFactory:
    def __init__(self, client: "CoreBotAuth"):
        self._client = client

    def photo(self, file: str | bytes):
        return InputMedia(self._client, "photo", file)

    def video(self, file: str | bytes):
        return InputMedia(self._client, "video", file)

@dataclass
class SuggestedPostParametersBuilder:
    _data: Dict[str, Any] = field(default_factory=dict)

    def currency(self, value: str):
        self._data["currency"] = value
        return self

    def amount(self, value: int):
        self._data["amount"] = value
        return self

    def build(self):
        return self._data

@dataclass
class LinkPreviewBuilder:
    _data: Dict[str, Any] = field(default_factory=dict)

    def is_disabled(self, value: bool):
        self._data["is_disabled"] = value
        return self

    def url(self, value: str):
        self._data["url"] = value
        return self

    def prefer_small_media(self, value: bool):
        self._data["prefer_small_media"] = value
        return self

    def prefer_large_media(self, value: bool):
        self._data["prefer_large_media"] = value
        return self

    def show_above_text(self, value: bool):
        self._data["show_above_text"] = value
        return self

    def build(self):
        if "prefer_small_media" in self._data and "prefer_large_media" in self._data:
            raise ValueError("Cannot set both small and large media preference")
        return self._data

@dataclass
class ReplyParametersBuilder:
    _data: Dict[str, Any] = field(default_factory=dict)

    def message_id(self, value: int):
        self._data["message_id"] = value
        return self

    def chat_id(self, value: Union[str, int]):
        self._data["chat_id"] = value
        return self

    def allow_sending_without_reply(self, value: bool):
        self._data["allow_sending_without_reply"] = value
        return self

    def quote(self, value: str):
        self._data["quote"] = value
        return self

    def quote_parse_mode(self, value: str = "MarkdownV2"):
        self._data["quote_parse_mode"] = value
        return self

    def build(self):
        return self._data

@dataclass
class InlineKeyboardBuilder:
    _rows: List[List[Dict[str, Any]]] = field(default_factory=list)
    _current_row: List[Dict[str, Any]] = field(default_factory=list)

    def _add(self, btn: Dict[str, Any]):
        self._current_row.append(btn)
        return self

    def url(self, text: str, url: str):
        return self._add({"text": text, "url": url})

    def style(self, text: str, style: str, **kw):
        return self._add({"text": text, "style": style, **kw})

    def callback(self, text: str, data: str):
        if len(data.encode()) > 64:
            raise ValueError("callback_data max 64 bytes")
        return self._add({"text": text, "callback_data": data})

    def copy_text(self, text: str, copy_text: str):
        return self._add({
            "text": text,
            "copy_text": {"text": copy_text}
        })

    def switch_inline_query_chosen_chat(self, text: str, **kw):
        _ALLOWED = {
            "query",
            "allow_user_chats",
            "allow_bot_chats",
            "allow_group_chats",
            "allow_channel_chats"
        }
        data = {k: v for k, v in kw.items() if k in _ALLOWED}
        return self._add({
            "text": text,
            "switch_inline_query_chosen_chat": data
        })

    def login(self, text: str, url: str):
        return self._add({
            "text": text,
            "login_url": {"url": url}
        })

    def pay(self, text: str, pay=False):
        return self._add({"text": text, "pay": pay})

    def webapp(self, text: str, url: str):
        return self._add({
            "text": text,
            "web_app": {"url": url}
        })

    def row(self):
        if self._current_row:
            self._rows.append(self._current_row)
            self._current_row = []
        return self

    def build(self):
        if self._current_row:
            self.row()
        return {"inline_keyboard": self._rows}

@dataclass
class ReplyKeyboardBuilder:
    _keyboard: List[List[Dict[str, Any]]] = field(default_factory=list)
    _row: List[Dict[str, Any]] = field(default_factory=list)
    _options: Dict[str, Any] = field(default_factory=dict)

    def text(self, value: str):
        self._row.append({"text": value})
        return self

    def row(self):
        if self._row:
            self._keyboard.append(self._row)
            self._row = []
        return self

    def resize_keyboard(self, value: bool = True):
        self._options["resize_keyboard"] = value
        return self

    def one_time_keyboard(self, value: bool = True):
        self._options["one_time_keyboard"] = value
        return self

    def selective(self, value: bool = True):
        self._options["selective"] = value
        return self

    def input_field_placeholder(self, value: str):
        self._options["input_field_placeholder"] = value
        return self

    def build(self):
        if self._row:
            self._keyboard.append(self._row)

        return {
            "keyboard": self._keyboard,
            **self._options
        }

class ButtonExamples:
    @staticmethod
    def url(text, url):
        return InlineKeyboardBuilder().url(text, url).build()

    @staticmethod
    def style(text, style, **kw):
        return InlineKeyboardBuilder().style(text, style, **kw).build()

    @staticmethod
    def callback(text, data):
        return InlineKeyboardBuilder().callback(text, data).build()

    @staticmethod
    def copy_text(text, copy_text):
        return InlineKeyboardBuilder().copy_text(text, copy_text).build()

@dataclass
class ResponseResult:
    data: Any
    def text(self):
        return self.data.choices[0].message.content

    def video_url(self, value=0):
        return self.data.video[value].url

    def pins_url(self, value=0):
        return self.data.pins[value].media.images.orig.url

    def capcut_url(self):
        return self.data.originalVideoUrl

    def aio_url(self, defaults=True):
        return self.data.links.video[0].url if defaults else self.data.links

    def threads_url(self, is_video: bool = True):
        return self.data.video if is_video else self.data.image

    def twitter_url(self, _type: str = "hd"):
        if _type == "hd":
            return self.data.url[0].hd
        if _type == "sd":
            return self.data.url[1].sd
        return self.data.url

    def image_bytes(self):
        return self.data.image_bytes

    def ig_url(self):
        return self.data.download

    def pins_urls(self):
        _list = []
        for x in self.data.pins.media_urls:
            if x.type == "image":
                _list.append(x.url)
            if x.type == "video":
                _list.append(x.url)
        return _list

    def tokens(self):
        return self.data.usage.total_tokens

    def model(self):
        return self.data.model

@dataclass
class RequestCall(Generic[T]):
    _client: "CoreBotAuth"
    _method: str
    _path: str
    _params: Dict[str, Any] = field(default_factory=dict)
    _response_model: Optional[Type[T]] = None

    def __getattr__(self, name):
        def setter(value):
            self._params[name] = value
            return self
        return setter

    async def execute(self, is_content: bool = False) -> T:
        raw = await (
            self._client._get(self._path, self._params, is_content)
            if self._method.upper() == "GET"
            else self._client._post(self._path, self._params, is_content)
        )

        if self._response_model is None:
            return raw  # type: ignore

        return self._response_model.model_validate(raw)  # type: ignore

    async def send(
        self,
        *,
        allow_object: bool = False,
        via_result: bool = False
    ) -> Any:
        result = await self.execute()
        if via_result:
            return ResponseResult(
                self._client.to_obj(result["data"])
            )
        else:
            return self._client.to_obj(result) if allow_object else result

    async def skip(self) -> Any:
        _result = await self.execute()
        if not _result["ok"] or not _result["data"]:
            return None
        return _result["ok"]

    async def json(self) -> Any:
        return await self.execute()

    async def pretty(self, indent: int = 2) -> str:
        data = await self.execute()
        if hasattr(data, "model_dump"):
            return json.dumps(data.model_dump(), indent=indent, ensure_ascii=False)
        return json.dumps(data, indent=indent, ensure_ascii=False)

class Keyboard:
    @staticmethod
    def inline():
        return InlineKeyboardBuilder()

    @staticmethod
    def reply():
        return ReplyKeyboardBuilder()

@dataclass
class CoreBotAuth:
    api_key: str
    base_url: str = "https://tgcore.ryzenths.dpdns.org"
    user_agent: str = "tgcore/1.0"
    timeout: float = 30.0

    _parse_mode: str | None = None
    _extra_headers: Dict[str, str] = field(default_factory=dict)
    _client: Optional[httpx.AsyncClient] = field(default=None, init=False, repr=False)
    kb: Keyboard = field(default_factory=Keyboard)

    def _ensure_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(timeout=self.timeout)
        return self._client

    async def aclose(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        h = {
            "x-api-key": self.api_key,
            "accept": "application/json",
            "user-agent": self.user_agent,
        }
        for k, v in self._extra_headers.items():
            h[k.lower()] = v
        if extra:
            for k, v in extra.items():
                h[k.lower()] = v
        return h

    def escape(self, text: str):
        return self.escape_md(text)

    def escape_md(self, text: str) -> str:
        _MD_V2_ESCAPE = r"_*[]()~`>#+-=|{}.!"
        return re.sub(f"([{re.escape(_MD_V2_ESCAPE)}])", r"\\\1", text)

    def set_markdown(self, mode: str | bool = True):
        if mode is True:
            self._parse_mode = "MarkdownV2"
        elif mode is False:
            self._parse_mode = None
        else:
            self._parse_mode = mode
        return self

    def set_header(self, key: str, value: str) -> "CoreBotAuth":
        self._extra_headers[key.lower()] = value
        return self

    def to_obj(self, everything):
        return Box(everything)

    def lw(self):
        return LinkPreviewBuilder()

    def rs(self):
        return ReplyParametersBuilder()

    def _raise_http_error(self, r: httpx.Response) -> None:
        if r.is_success:
            return
        try:
            payload = r.json()
        except Exception:
            payload = r.text[:800]
        raise RuntimeError(f"HTTP {r.status_code}: {payload}")

    def is_url(self, text):
        match = re.search(r"https://\S+", text)
        return match.group(0) if match else None

    def writer(
        self,
        prefix: str = "custom.jpg",
        *,
        cbytes: bytes | str,
        is_base64: bool = False
    ):
        allowed_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
        if not prefix.lower().endswith(allowed_extensions):
            return None
        path = f"tgcore-{uuid.uuid4()}-{prefix}"
        with open(path, "wb") as f:
            if is_base64:
                dd = base64.b64decode(cbytes)
                f.write(dd)
            else:
                f.write(cbytes)
        return path

    async def _post(
        self,
        path: str,
        payload: Dict[str, Any],
        headers: Dict[str, str] | None = None,
        is_content: bool = False,
    ) -> Union[Dict[str, Any], bytes]:
        payload = dict(payload or {})
        path = _format_path_and_pop_params(path, payload)

        c = self._ensure_client()
        url = self.base_url.rstrip("/") + path

        if self._parse_mode and "parse_mode" not in payload:
            payload["parse_mode"] = self._parse_mode

        files = _extract_files(payload)

        if files:
            data = _normalize_form_data(payload)
            r = await c.post(url, data=data, files=files, headers=self._headers(headers))
        else:
            r = await c.post(url, json=payload, headers=self._headers(headers))

        self._raise_http_error(r)
        return r.content if is_content else r.json()

    async def fetch_post(self, path: str, **kw):
        headers = kw.pop("headers", None)
        check_errors = kw.pop("check_errors", False)
        ok = await self._post(
            path=path,
            payload=kw,
            headers=headers
        )
        if check_errors:
            obj = self.to_obj(ok)
            if not obj.ok or not obj.data:
                return None
            return obj
        else:
            return ok

    async def _get(
        self,
        path: str,
        params: Dict[str, Any],
        headers: Dict[str, str] | None = None,
        is_content: bool = False,
    ) -> Union[Dict[str, Any], bytes]:
        params = dict(params or {})
        path = _format_path_and_pop_params(path, params)

        c = self._ensure_client()
        url = self.base_url.rstrip("/") + path
        r = await c.get(url, params=params, headers=self._headers(headers))

        self._raise_http_error(r)
        return r.content if is_content else r.json()
