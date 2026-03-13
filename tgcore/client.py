# Copyright 2026 Randy W
# Licensed under the Apache License, Version 2.0

"""
Github Author: https://github.com/TeamKillerX/
Code: @zxyeor

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
"""

from __future__ import annotations

import os
from typing import Optional

from .core import CoreBotAuth, MediaFactory
from .methods import Methods
from .platform import Platform
from .default import DefaultMethod
from .telegram_namespace import TelegramNamespace


class Client(CoreBotAuth):
    def __init__(self, api_key=None, **kw):
        api_key = api_key or os.getenv("TGCORE_API_KEY")
        if not api_key:
            raise ValueError("TGCore API key required")

        super().__init__(api_key, **kw)

        self.raw = Methods(self)
        self.use = DefaultMethod(self)
        self.platform = Platform(self)
        self.media: MediaFactory = MediaFactory(self)
        self.telegram = TelegramNamespace(self)
