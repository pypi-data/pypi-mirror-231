from pathlib import Path
from bridgeobjects import load_pbn

from .. import next_card
from ..tests.utilities import get_board

BOARD_PATH = Path('tests', 'test_data', 'first_seat_declarer.pbn')

boards = load_pbn(BOARD_PATH)[0].boards


def test_select_suit_with_cards():
    """ENsure an suit with no cards is not selected."""
    board = get_board(boards, 0)
    next_card(board).name  # Seem to need to play this card before we get the correct card
    assert next_card(board).name[1] != 'D'
