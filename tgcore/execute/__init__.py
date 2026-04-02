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


class Execute(BaseMethod):
    def create(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v3/request",
            kw
        )

    def run(self, **KW):
        return RequestCall(
            self._client,
            "POST",
            f"/api/v3/request/{request_id}/execute",
            kw
        )

    def get(self, request_id: str):
        return RequestCall(
            self._client,
            "GET",
            f"/api/v3/request/{request_id}",
            {}
        )

    def delete(self, request_id: str):
        return RequestCall(
            self._client,
            "DELETE",
            f"/api/v3/request/{request_id}",
            {}
        )

class Request:
    def __init__(self, client):
        self.execute = Execute(client)
