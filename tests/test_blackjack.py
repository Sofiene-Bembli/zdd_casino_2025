import pytest
from casino.blackjack import count_cards

def test_count_cards_no_aces():
    cards = ['10', '7', '3']
    assert count_cards(cards) == 20

@pytest.mark.parametrize("cards, expected_total", [ 
    (["2", "3"], 5),
    (["A", "A"], 12),
    (["A", "K"], 21),
    (["A", "9"], 20),
    (["A", "4"], 15)
])

def test_count_cards_with_aces(cards, expected_total):
   assert count_cards(cards) == expected_total