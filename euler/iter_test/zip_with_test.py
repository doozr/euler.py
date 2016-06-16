from euler.iter import zip_with


def test_zip_with_acts_as_map_with_one_input():
    assert list(zip_with(lambda x: x + 1, [1, 2, 3])) == [2, 3, 4]


def test_zip_with_passes_multiple_inputs():
    assert list(zip_with(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])) == [5, 7, 9]


def test_zip_with_accepts_arbitrary_number_of_inputs():
    assert list(zip_with(lambda w, x, y, z: w + x + y + z, [1], [2], [3], [4])) == [10]


def test_zip_with_truncates_to_the_shortest_input():
    assert list(zip_with(lambda x, y, z: x + y + z, [1, 2, 3], [1, 2], [1, 2, 3, 4])) == [3, 6]
