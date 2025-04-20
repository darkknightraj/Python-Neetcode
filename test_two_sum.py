from TwoSumHash import TwoSum  # replace 'your_filename' with the actual filename

def test_basic_case():
    arr = [2, 8, 11, 15]
    target = 19
    assert TwoSum(arr, target) == [1, 2]

def test_no_solution():
    arr = [1, 2, 3, 4]
    target = 10
    assert TwoSum(arr, target) == [-1, -1]

def test_negative_numbers():
    arr = [-3, 4, 3, 90]
    target = 0
    assert TwoSum(arr, target) == [0, 2]

def test_duplicate_numbers():
    arr = [3, 3]
    target = 6
    assert TwoSum(arr, target) == [0, 1]

def test_empty_array():
    arr = []
    target = 5
    assert TwoSum(arr, target) == [-1, -1]
