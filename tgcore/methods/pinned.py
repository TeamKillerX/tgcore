# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

# Github Author: https://github.com/TeamKillerX/
# Code: @zxyeor

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

from ..core import RequestCall
from .base import BaseMethod


class Pinned(BaseMethod):
    def pinChatMessage(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/pinChatMessage",
            kw
        )

    def unpinChatMessage(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/unpinChatMessage",
            kw
        )

    def unpinAllChatMessages(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/unpinAllChatMessages",
            kw
        )
