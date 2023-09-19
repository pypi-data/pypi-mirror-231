from pathlib import Path
from bridgeobjects import load_pbn
from bfgdealer import Board


from ..src.player import Player
from ..tests.utilities import get_board

BOARD_PATH = Path('tests', 'test_data', 'player.pbn')

boards = load_pbn(BOARD_PATH)[0].boards
