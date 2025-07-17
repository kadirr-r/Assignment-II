from bubble_sort import bubble_sort

def test_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]

def test_duplicates():
    assert bubble_sort([4, 5, 3, 4]) == [3, 4, 4, 5]
