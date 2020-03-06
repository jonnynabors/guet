from typing import List

from guet.commands.command import Command
from guet.commands.command_factory import CommandFactoryMethod
from guet.context.context import Context
from guet.settings.settings import Settings


class CommandFactoryMethodWithContext(CommandFactoryMethod):
    def __init__(self):
        super().__init__()
        self.context = Context.instance()

    def short_help_message(self) -> str:
        raise NotImplementedError()

    def build(self, args: List[str], settings: Settings) -> Command:
        raise NotImplementedError()