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


class Chat(BaseMethod):
    def getChat(self, **kw):
        return RequestCall(
            _client=self._client,
            _method="GET",
            _path="/api/v2/getChat",
            _params=kw
        )

    def getChatAdministrators(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/getChatAdministrators",
            kw
        )

    def getChatMember(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/getChatMember",
            kw
        )

    def exportChatInviteLink(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/exportChatInviteLink",
            kw
        )

    def setChatPermissions(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/setChatPermissions",
            kw
        )
