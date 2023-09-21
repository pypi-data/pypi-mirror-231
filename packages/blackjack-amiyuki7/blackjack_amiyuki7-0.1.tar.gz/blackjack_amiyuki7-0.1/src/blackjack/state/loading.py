from __future__ import annotations
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from ..app import App

from glob import glob

from ..app import State


class AssetLoader:
    def __init__(self) -> None:
        self.to_load = self.all_assets()
        self.expected_files = len(self.to_load)
        print("[DEBUG]: EXPECTED FILES", self.expected_files)

    @staticmethod
    def all_assets() -> List[str]:
        return [path for path in glob("card_png/**/*.png", recursive=True)]


class Loading(State):
    def __init__(self, ctx: App) -> None:
        self.loader = AssetLoader()

        super().__init__(ctx)

    def update(self) -> None:
        self.ctx.lucky += 1

    def render(self) -> None:
        pass

    def pend(self) -> None:
        super().pend()
