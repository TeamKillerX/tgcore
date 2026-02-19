# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

# Github Author: https://github.com/TeamKillerX/
# Code: @zxyeor

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

from .base import BaseMethod

class Message(BaseMethod):
    async def sendMessage(self, **data):
        return await self._client._post(
            "/api/v2/sendMessage",
            data
        )

    async def sendPhoto(self, **data):
        return await self._client._post(
            "/api/v2/sendPhoto",
            data
        )

    async def sendVideo(self, **data):
        return await self._client._post(
            "/api/v2/sendVideo",
            data
        )

    async def sendMediaGroup(self, **data):
        return await self._client._post(
            "/api/v2/sendMediaGroup",
            data
        )

    async def pinChatMessage(self, **data):
        return await self._client._post(
            "/api/v2/pinChatMessage",
            data
        )
  
    async def sendAnimation(self, **data):
        return await self._client._post(
            "/api/v2/sendAnimation",
            data
        )
  
    async def forwardMessages(self, **data):
        return await self._client._post(
            "/api/v2/forwardMessages",
            data
        )

    async def forwardMessage(self, **data):
        return await self._client._post(
            "/api/v2/forwardMessage",
            data
        )

    async def deleteMessages(self, **data):
        return await self._client._post(
            "/api/v2/deleteMessages",
            data
        )

    async def deleteMessage(self, **data):
        return await self._client._post(
            "/api/v2/deleteMessage",
            data
        )

    async def declineChatJoinRequest(self, **data):
        return await self._client._post(
            "/api/v2/declineChatJoinRequest",
            data
        )

    async def copyMessages(self, **data):
        return await self._client._post(
            "/api/v2/copyMessages",
            data
        )
  
    async def copyMessage(self, **data):
        return await self._client._post(
            "/api/v2/copyMessage",
            data
        )

    async def banChatSenderChat(self, **data):
        return await self._client._post(
            "/api/v2/banChatSenderChat",
            data
        )

    async def banChatMember(self, **data):
        return await self._client._post(
            "/api/v2/banChatMember",
            data
        )
  
    async def approveChatJoinRequest(self, **data):
        return await self._client._post(
            "/api/v2/approveChatJoinRequest",
            data
        )
