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

from ..core import RequestCall
from ..models import BetterResponse, WebhookInfo
from .base import BaseMethod


class Webhook(BaseMethod):
    def getWebhookInfo(self) -> RequestCall[BetterResponse[WebhookInfo]]:
        return RequestCall(
            _client=self._client,
            _method="GET",
            _path="/api/v2/getWebhookInfo",
            _params={},
            _response_model=BetterResponse[WebhookInfo]
        )
