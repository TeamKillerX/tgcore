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

from __future__ import annotations

import os
from typing import Optional

from .chats import Chats
from .core import CoreBotAuth, MediaFactory
from .default import DefaultMethod
from .methods import Methods
from .monitors import UptimeRobot
from .platform import Platform
from .quotes import Quotes
from .services import Services
from .telegram_namespace import TelegramNamespace
from .translate import CustomTranslate


class Client(CoreBotAuth):
    def __init__(
        self,
        api_key=None,
        bearer_token=None,
        is_bearer=False,
        **kw
    ):
        api_key = api_key or os.getenv("TGCORE_API_KEY")
        super().__init__(
            api_key=api_key,
            bearer_token=bearer_token,
            is_bearer=is_bearer,
            **kw
        )
        self.raw = Methods(self)
        self.ai = Chats(self)
        self.monitor = UptimeRobot(self)
        self.translate = CustomTranslate(self)
        self.services = Services(self)
        self.quotes = Quotes(self)
        self.use = DefaultMethod(self)
        self.platform = Platform(self)
        self.media: MediaFactory = MediaFactory(self)
        self.telegram = TelegramNamespace(self)
