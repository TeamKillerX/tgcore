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


class Capcut(BaseMethod):
    def download(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/web/capcut/download",
            kw
        )
