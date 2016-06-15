from euler.iter import take_while_incl


def test_take_until_returns_subset_of_list():
    assert list(take_while_incl(lambda x: x != 3, [1, 2, 3, 4, 5])) == [1, 2, 3]


def test_take_until_returns_subset_of_generator():
    assert list(take_while_incl(lambda x: x != 3, (x for x in range(1, 6)))) == [1, 2, 3]


def test_take_until_returns_subset_of_iter():
    assert list(take_while_incl(lambda x: x != 3, iter([1, 2, 3, 4, 5]))) == [1, 2, 3]


def test_take_until_stops_at_first_match():
    assert list(take_while_incl(lambda x: x != 3, [1, 2, 3, 4, 3])) == [1, 2, 3]


def test_take_until_returns_full_sequence_if_no_match():
    assert list(take_while_incl(lambda x: x != 3, [1, 2, 2, 4, 5])) == [1, 2, 2, 4, 5]

