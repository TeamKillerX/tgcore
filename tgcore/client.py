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

from .core import CoreBotAuth
from .telegram_namespace import TelegramNamespace


class Client(CoreBotAuth):
    def __init__(self, api_key: str, **kw):
        super().__init__(api_key, **kw)
        self.telegram = TelegramNamespace(self)
