from unittest import TestCase, mock
from unittest.mock import Mock, MagicMock

from guet.commands.strategy_command import StrategyCommand
from guet.commands.strategy import CommandStrategy
from guet.settings.settings import Settings


class TestStrategyCommand(TestCase):

    def test_execute_calls_the_strategy_apply(self):
        strategy = MagicMock(CommandStrategy)
        strategy.apply = MagicMock()
        command = StrategyCommand(strategy)
        command.execute()
        strategy.apply.assert_called_once()