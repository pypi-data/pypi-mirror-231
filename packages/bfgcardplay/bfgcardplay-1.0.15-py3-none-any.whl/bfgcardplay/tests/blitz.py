""" Generate and play random hands until it breaks."""
import sys
import os
from termcolor import cprint
import logging

from bridgeobjects import Card, Trick, SEATS
from bfgdealer import Dealer, Board

from bfgcardplay.src.suggested_card import next_card
# from application.app.folder.file import func_name

MODULE_COLOUR = 'blue'
MAX_HANDS = 10**6


def main():
    # logging.disable(logging.CRITICAL)
    count = 0
    while count < MAX_HANDS:
        board = Dealer().deal_random_board()
        board.auction = board.get_auction()
        board.contract = board.get_contract()
        if not board.contract.name:
            continue

        display_board(board, count)

        for _ in range(52):
            card = next_card(board)
            update_board_after_cardplay(board, card)
        # halt()

        count += 1


def display_board(board, count):
    os.system('clear')
    print(f"{count + 1} {'-'*50}")
    cprint('\n'.join(board.board_to_pbn()), MODULE_COLOUR)


def update_board_after_cardplay(board: Board, card: Card) -> Board:
    trick = board.tricks[-1]
    current_player = get_current_player(trick)
    if card and card in board.hands[current_player].unplayed_cards:
        add_card_to_trick(board, trick, card)
        board.hands[current_player].unplayed_cards.remove(card)
    return board


def add_card_to_trick(board, trick, card):
    if card in trick.cards:
        return
    trick.cards.append(card)
    if len(trick.cards) == 4:
        complete_trick(board, trick)


def complete_trick(board: Board, trick: Trick) -> str:
    """complete the trick update the board and return trick winner."""
    trick.complete(board.contract.denomination)
    winner = trick.winner
    trick = Trick(leader=winner)
    board.tricks.append(trick)
    return winner


def get_current_player(trick: Trick) -> str:
    """Return the current player from the trick."""
    if len(trick.cards) == 4:
        return trick.winner
    leader_index = SEATS.index(trick.leader)
    current_player = (leader_index + len(trick.cards)) % 4
    return SEATS[current_player]


def halt():
    result = input('-->')
    if result in ['Q', 'q']:
        sys.exit()


if __name__ == '__main__':
    main()
