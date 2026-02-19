# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

# Github Author: https://github.com/TeamKillerX/
# Code: @zxyeor

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

from .base import BaseMethod

class Stickers(BaseMethod):
    async def addStickerToSet(self, **data):
        return await self._client._post(
            "/api/v2/addStickerToSet",
            data
        )
    async def deleteStickerFromSet(self, **data):
        return await self._client._post(
            "/api/v2/deleteStickerFromSet",
            data
        )
  
    async def deleteStickerSet(self, **data):
        return await self._client._post(
            "/api/v2/deleteStickerSet",
            data
        )
  
    async def createNewStickerSet(self, **data):
        return await self._client._post(
            "/api/v2/createNewStickerSet",
            data
        )

    async def getCustomEmojiStickers(self, **data):
        return await self._client._post(
            "/api/v2/getCustomEmojiStickers",
            data
        )

    async def getStickerSet(self, **data):
        return await self._client._post(
            "/api/v2/getStickerSet",
            data
        )

    async def replaceStickerInSet(self, **data):
        return await self._client._post(
            "/api/v2/replaceStickerInSet",
            data
        )

    async def setCustomEmojiStickerSetThumbnail(self, **data):
        return await self._client._post(
            "/api/v2/setCustomEmojiStickerSetThumbnail",
            data
        )

    async def sendSticker(self, **data):
        return await self._client._post(
            "/api/v2/sendSticker",
            data
        )
