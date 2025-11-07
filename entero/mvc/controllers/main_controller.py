from __future__ import annotations

from typing import Optional


class MainController:
    def __init__(self, root):
        self.root = root
        self.view: Optional[object] = None

    def attach_view(self, view) -> None:
        self.view = view


