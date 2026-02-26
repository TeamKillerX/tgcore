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


class Topic(BaseMethod):
    def createForumTopic(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/createForumTopic",
            kw
        )

    def editForumTopic(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/editForumTopic",
            kw
        )

    def editGeneralForumTopic(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/editGeneralForumTopic",
            kw
        )

    def hideGeneralForumTopic(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/hideGeneralForumTopic",
            kw
        )

    def deleteForumTopic(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/deleteForumTopic",
            kw
        )

    def closeForumTopic(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/closeForumTopic",
            kw
        )

    def closeGeneralForumTopic(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/closeGeneralForumTopic",
            kw
        )

    def unpinAllForumTopicMessages(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/unpinAllForumTopicMessages",
            kw
        )

    def unpinAllGeneralForumTopicMessages(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v2/unpinAllGeneralForumTopicMessages",
            kw
        )
