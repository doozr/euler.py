from euler.iter import take_while_incl


def test_take_until_returns_subset_of_sequence():
    assert list(take_while_incl(lambda x: x != 3, [1, 2, 3, 4, 5])) == [1, 2, 3]


def test_take_until_stops_at_first_match():
    assert list(take_while_incl(lambda x: x != 3, [1, 2, 3, 4, 3])) == [1, 2, 3]


def test_take_until_returns_full_sequence_if_no_match():
    assert list(take_while_incl(lambda x: x != 3, [1, 2, 2, 4, 5])) == [1, 2, 2, 4, 5]


def test_take_until_returns_empty_sequence_if_input_in_empty():
    assert list(take_while_incl(lambda x: x != 3, [])) == []
