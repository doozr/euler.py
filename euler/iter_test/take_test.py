from euler.iter import take


def test_take_returns_subset_of_list():
    assert list(take([1, 2, 3, 4, 5], 3)) == [1, 2, 3]


def test_take_returns_subset_of_generator():
    assert list(take((x for x in range(1, 6)), 3)) == [1, 2, 3]


def test_take_returns_subset_of_iter():
    assert list(take(iter([1, 2, 3, 4, 5]), 3)) == [1, 2, 3]


def test_take_returns_empty_sequence_if_length_zero():
    assert list(take([1, 2, 3, 4, 5], 0)) == []


def test_take_raises_an_error_if_length_lt_zero():
    try:
        take([1, 2, 3, 4, 5], -1)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_take_returns_full_sequence_if_length_greater_gt_sequence():
    assert list(take([1, 2, 3, 4, 5], 10)) == [1, 2, 3, 4, 5]
