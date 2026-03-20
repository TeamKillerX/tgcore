# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

# Github Author: https://github.com/TeamKillerX/
# Code: @zxyeor

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

from ..core import RequestCall
from ..methods.base import BaseMethod


class OnApp(BaseMethod):
    def app(self, name: str = None, **kw):
        return RequestCall(self._client, "POST", f"/api/web/{name}", kw)

class Default(BaseMethod):
    def route(
        self,
        name: str = None,
        custom: str = None,
        **kw
    ):
        return RequestCall(self._client, "POST", f"/api/web/{name}/{custom}", kw)

    def endpoint(self, path: str, use: bool = True, **kw):
        return RequestCall(self._client, "POST", path, kw) if use else RequestCall(self._client, "GET", path, {})
