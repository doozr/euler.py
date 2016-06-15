from euler.iter import every


def test_every_returns_portions_of_list():
    assert list(every([1], 1)) == [1]


def test_every_returns_portions_of_generator():
    assert list(every((x for x in [1]), 1)) == [1]


def test_every_returns_portions_of_iter():
    assert list(every(iter([1]), 1)) == [1]


def test_every_returns_every_item_if_step_is_one():
    assert list(every([1, 2, 3, 4, 5, 6], 1)) == [1, 2, 3, 4, 5, 6]


def test_every_returns_every_nth_value_if_step_gt_one():
    assert list(every([1, 2, 3, 4, 5, 6], 3)) == [3, 6]


def test_every_starts_on_the_specified_value_skip_is_lt_step():
    assert list(every([1, 2, 3, 4, 5, 6], 3, 1)) == [2, 5]


def test_every_starts_on_the_specified_value_skip_is_eq_step():
    assert list(every([1, 2, 3, 4, 5, 6, 7], 3, 3)) == [4, 7]


def test_every_starts_on_the_specified_value_skip_is_gt_step():
    assert list(every([1, 2, 3, 4, 5, 6, 7, 8], 3, 4)) == [5, 8]


def test_every_starts_on_the_specified_value_skip_is_eq_zero():
    assert list(every([1, 2, 3, 4, 5, 6], 3, 0)) == [1, 4]


def test_every_raises_value_error_if_step_eq_zero():
    try:
        list(every([1, 2, 3], 0))
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_every_raises_value_error_if_step_lt_zero():
    try:
        list(every([1, 2, 3], -1))
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_every_raises_value_error_if_skip_lt_zero():
    try:
        list(every([1, 2, 3], 1, -1))
        assert False, "Expected ValueError"
    except ValueError:
        pass
