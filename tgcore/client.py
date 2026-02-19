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

from .core import CoreBotAuth
from .methods import Methods
from .telegram_namespace import TelegramNamespace


class Client(CoreBotAuth):
    def __init__(self, api_key: str | None = None, **kwargs):
        api_key = api_key or os.getenv("TGCORE_API_KEY")
        if not api_key:
            raise ValueError("TGCore API key required. Pass api_key= or set TGCORE_API_KEY env.")
        super().__init__(api_key, **kwargs)

        self.raw = Methods(self)
        self.telegram = TelegramNamespace(self)
