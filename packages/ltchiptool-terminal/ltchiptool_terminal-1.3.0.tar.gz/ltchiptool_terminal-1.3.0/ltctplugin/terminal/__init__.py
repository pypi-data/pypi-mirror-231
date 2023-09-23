#  Copyright (c) Kuba Szczodrzyński 2023-5-22.

from typing import Any, Dict

from ltctplugin.base import PluginBase


class Plugin(PluginBase):
    @property
    def title(self) -> str:
        return "Terminal"

    @property
    def has_cli(self) -> bool:
        return False

    @property
    def has_gui(self) -> bool:
        return True

    def build_cli(self, *args, **kwargs) -> Dict[str, Any]:
        return dict()

    def build_gui(self, *args, **kwargs) -> Dict[str, Any]:
        from .gui import TerminalPanel

        return dict(
            upk=TerminalPanel,
        )


entrypoint = Plugin

__all__ = [
    "entrypoint",
]
