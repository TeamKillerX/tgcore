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


class Stickers(BaseMethod):
    def addStickerToSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/addStickerToSet",
            kw
        )

    def deleteStickerFromSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/deleteStickerFromSet",
            kw
        )

    def deleteStickerSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/deleteStickerSet",
            kw
        )

    def createNewStickerSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/createNewStickerSet",
            kw
        )

    def getCustomEmojiStickers(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/getCustomEmojiStickers",
            kw
        )

    def getStickerSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/getStickerSet",
            kw
        )

    def replaceStickerInSet(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/replaceStickerInSet",
            kw
        )

    def setCustomEmojiStickerSetThumbnail(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/setCustomEmojiStickerSetThumbnail",
            kw
        )

    def sendSticker(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/sendSticker",
            kw
        )
