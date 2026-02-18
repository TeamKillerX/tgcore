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

import json
import re
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

import httpx

T = TypeVar("T")

_PATH_PARAM_RE = re.compile(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}")

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

@dataclass
class KeyboardBuilder:
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
class RequestCall(Generic[T]):
    _client: "CoreBotAuth"
    _method: str
    _path: str
    _params: Dict[str, Any]

    async def execute(self) -> T:
        if self._method == "GET":
            return await self._client._get(self._path, self._params)  # type: ignore
        return await self._client._post(self._path, self._params)  # type: ignore

    async def pretty(self, indent: int = 2) -> str:
        data = await self.execute()
        try:
            return json.dumps(data, indent=indent, ensure_ascii=False)
        except TypeError:
            return str(data)

@dataclass
class CoreBotAuth:
    api_key: str
    base_url: str = "https://services-pro.ryzenths.dpdns.org"
    timeout: float = 30.0

    def _headers(self) -> Dict[str, str]:
        return {"x-api-key": self.api_key}

    async def _post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(payload or {})
        path = _format_path_and_pop_params(path, payload)

        async with httpx.AsyncClient(timeout=self.timeout) as c:
            try:
                r = await c.post(self.base_url + path, json=payload, headers={**self._headers(), "Content-Type": "application/json"})
                if r.status_code == 500:
                    raise Exception(f"Internal Server Status: {r.status_code} Error")
                return r.json()
            except httpx.HTTPStatusError as e:
                raise Exception("Internal Server Error") from e

    async def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        params = dict(params or {})
        path = _format_path_and_pop_params(path, params)

        async with httpx.AsyncClient(timeout=self.timeout) as c:
            r = await c.get(self.base_url + path, params=params, headers=self._headers())
            r.raise_for_status()
            return r.json()
