# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=undefined-variable
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

# Github Author: https://github.com/TeamKillerX/
# Code: @zxyeor

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")

class ResponseTo(BaseModel):
    prefix: str
    cbytes: bytes | str
    is_base64: bool = False

class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: Optional[str] = None
    language_code: Optional[str] = None
    is_premium: Optional[bool] = None
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None
    can_connect_to_business: Optional[bool] = None
    has_main_web_app: Optional[bool] = None
    has_topics_enabled: Optional[bool] = None
    allows_users_to_create_topics: Optional[bool] = None

class WebhookInfo(BaseModel):
    url: str
    has_custom_certificate: Optional[bool] = None
    pending_update_count: Optional[int] = None
    last_error_date: Optional[int] = None
    last_error_message: Optional[str] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[str]] = None


class BetterResponse(BaseModel, Generic[T]):
    ok: bool
    data: Optional[T] = None
    error: Optional[str] = None

class GetMeResponse(BaseModel):
    ok: bool
    data: User
