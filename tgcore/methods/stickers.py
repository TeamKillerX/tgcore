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

class Stickers(BaseMethod):
    async def addStickerToSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/addStickerToSet",
            kw
        )

    async def deleteStickerFromSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/deleteStickerFromSet",
            kw
        )
  
    async def deleteStickerSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/deleteStickerSet",
            kw
        )
  
    async def createNewStickerSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/createNewStickerSet",
            kw
        )

    async def getCustomEmojiStickers(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/getCustomEmojiStickers",
            kw
        )

    async def getStickerSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/getStickerSet",
            kw
        )

    async def replaceStickerInSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/replaceStickerInSet",
            kw
        )

    async def setCustomEmojiStickerSetThumbnail(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/setCustomEmojiStickerSetThumbnail",
            kw
        )

    async def sendSticker(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendSticker",
            kw
        )
