from tasks_week2 import sum_positive, unique_words, find_max

def test_sum_positive_mixed():
    assert sum_positive([1, -2, 3, -4]) == 4

def test_sum_positive_empty():
    assert sum_positive([]) == 0

def test_unique_words_sorted_lowercase():
    assert unique_words("Bob bob Alice") == ["alice", "bob"]

def test_find_max_positive():
    assert find_max([3, 7, 1]) == 7

def test_find_max_empty():
    assert find_max([]) is None