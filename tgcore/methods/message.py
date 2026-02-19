# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

# Github Author: https://github.com/TeamKillerX/
# Code: @zxyeor

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

from .base import BaseMethod
from ..core import RequestCall

class Message(BaseMethod):
    def GetMe(self, **kw):
        return RequestCall(
            self._client,
            "GET",
            "/api/v2/getme",
            kw
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

    def sendVideo(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendVideo",
            kw
        )

    def sendMediaGroup(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendMediaGroup",
            kw
        )

    def pinChatMessage(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/pinChatMessage",
            kw
        )

    def sendAnimation(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendAnimation",
            kw
        )
        
    def forwardMessages(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/forwardMessages",
            kw
        )

    def forwardMessage(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/forwardMessage",
            kw
        )

    def deleteMessages(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/deleteMessages",
            kw
        )

    def deleteMessage(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/deleteMessage",
            kw
        )

    def declineChatJoinRequest(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/declineChatJoinRequest",
            kw
        )

    def copyMessages(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/copyMessages",
            kw
        )
  
    def copyMessage(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/copyMessage",
            kw
        )

    def banChatSenderChat(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/banChatSenderChat",
            kw
        )

    def banChatMember(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/banChatMember",
            kw
        )
  
    def approveChatJoinRequest(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/approveChatJoinRequest",
            kw
        )
