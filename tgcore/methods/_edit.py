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


class Edit(BaseMethod):
    def editMessageMedia(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/editMessageMedia",
            kw
        )

    def editMessageText(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/editMessageText",
            kw
        )

    def editMessageReplyMarkup(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/editMessageReplyMarkup",
            kw
        )

    def editMessageChecklist(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/editMessageChecklist",
            kw
        )
