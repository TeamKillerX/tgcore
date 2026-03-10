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


class Downloader(BaseMethod):
    def facebookDownload(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/web/facebook/download",
            kw
        )

    def tiktokDownload(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/web/tiktok/download",
            kw
        )

    def pinterestDownload(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/web/pinterest/download",
            kw
        )
