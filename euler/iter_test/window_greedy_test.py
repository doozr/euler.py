from euler.iter import window_greedy


def test_window_greedy_returns_all_sub_lists():
    assert list(window_greedy([1, 2, 3, 4, 5], 3)) == [[1], [1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5], [5]]


def test_window_greedy_raises_error_if_length_is_zero():
    try:
        next(window_greedy([1, 2, 3], 0))
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_window_greedy_raises_error_if_length_is_lt_zero():
    try:
        next(window_greedy([1, 2, 3], -1))
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_window_greedy_returns_full_sequence_if_length_gt_sequence():
    assert list(window_greedy([1, 2, 3], 5)) == [[1], [1, 2], [1, 2, 3], [2, 3], [3]]
