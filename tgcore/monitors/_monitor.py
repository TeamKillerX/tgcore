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
from ..methods.base import BaseMethod


class MonitorsGet(BaseMethod):
    def get(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v3/monitors",
            kw
        )

class MonitorsCreate(BaseMethod):
    def create(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            "/api/v3/monitor/create",
            kw
        )

class MonitorsUptimeStats(BaseMethod):
    def uptime_stats(self, **kw):
        return RequestCall(
            self._client,
            "POST",
            f"/api/v3/monitor/uptime-stats",
            kw
        )

class MonitorsIdUptimeStats(BaseMethod):
    def uptime_stats_id(self, id: int, **kw):
        return RequestCall(
            self._client,
            "POST",
            f"/api/v3/monitor/{id}/uptime-stats",
            kw
        )

class MonitorsIdGet(BaseMethod):
    def id(self, id: int):
        return RequestCall(
            self._client,
            "GET",
            f"/api/v3/monitor/{id}",
            {}
        )

class MonitorsIdReset(BaseMethod):
    def reset(self, id: int):
        return RequestCall(
            self._client,
            "POST",
            f"/api/v3/monitor/{id}/reset",
            {}
        )

class MonitorsIdPause(BaseMethod):
    def pause(self, id: int):
        return RequestCall(
            self._client,
            "POST",
            f"/api/v3/monitor/{id}/pause",
            {}
        )

class MonitorsIdStart(BaseMethod):
    def start(self, id: int):
        return RequestCall(
            self._client,
            "POST",
            f"/api/v3/monitor/{id}/start",
            {}
        )

class MonitorsIdUpdate(BaseMethod):
    def update(self, id: int, **kw):
        return RequestCall(
            self._client,
            "PATCH",
            f"/api/v3/monitor/{id}",
            kw
        )
