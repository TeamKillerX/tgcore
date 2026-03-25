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
from ..models import BetterResponse, User
from .base import BaseMethod


class Message(BaseMethod):
    def getMe(self) -> RequestCall[BetterResponse[User]]:
        return RequestCall(
            _client=self._client,
            _method="GET",
            _path="/api/v2/getMe",
            _params={},
            _response_model=BetterResponse[User]
        )
    def sendMessage(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendMessage",
            kw
        )

    def sendPhoto(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendPhoto",
            kw
        )

    def sendPhotoUpload(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendPhoto/upload",
            kw
        )

    def sendVideo(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendVideo",
            kw
        )

    def sendVideoUpload(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendVideo/upload",
            kw
        )

    def sendMediaGroup(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendMediaGroup",
            kw
        )

    def sendAnimation(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendAnimation",
            kw
        )

    def sendPoll(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendPoll",
            kw
        )

    def sendChecklist(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendChecklist",
            kw
        )

    def sendVoice(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendVoice",
            kw
        )

    def sendMessageDraft(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendMessageDraft",
            kw
        )

    def sendChatAction(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendChatAction",
            kw
        )
