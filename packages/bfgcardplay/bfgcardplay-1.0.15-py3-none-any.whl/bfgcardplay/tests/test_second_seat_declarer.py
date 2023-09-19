from pathlib import Path
from bridgeobjects import load_pbn

from .. import next_card
from ..tests.utilities import get_board

BOARD_PATH = Path('tests', 'test_data', 'second_seat_declarer.pbn')

boards = load_pbn(BOARD_PATH)[0].boards


def test_play_partners_suit():
    """Do not play high card when innappropriate."""
    board = get_board(boards, 0)
    assert next_card(board).name == '7H'


def test_do_not_signal_with_honour():
    """Do not signal with a losing honour."""
    board = get_board(boards, 1)
    assert next_card(board).name != 'KS'
