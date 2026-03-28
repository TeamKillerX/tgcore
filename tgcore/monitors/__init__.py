# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=undefined-variable
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

from ._monitor import (
    MonitorsCreate,
    MonitorsGet,
    MonitorsIdGet,
    MonitorsIdPause,
    MonitorsIdReset,
    MonitorsIdStart,
    MonitorsIdUpdate,
    MonitorsIdUptimeStats,
    MonitorsUptimeStats,
)


class UptimeRobot(
    MonitorsGet,
    MonitorsCreate
    MonitorsUptimeStats
    MonitorsIdUptimeStats
    MonitorsIdGet
    MonitorsIdReset
    MonitorsIdPause
    MonitorsIdStart
    MonitorsIdUpdate
):
    pass
