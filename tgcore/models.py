# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

# Github Author: https://github.com/TeamKillerX/
# Code: @zxyeor

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: Optional[str] = None

class BetterResponse(BaseModel, Generic[T]):
    ok: bool
    data: Optional[T] = None
    error: Optional[str] = None

class GetMeResponse(BaseModel):
    ok: bool
    data: User
