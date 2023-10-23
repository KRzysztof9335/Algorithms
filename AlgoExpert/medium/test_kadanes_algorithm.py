from medium.kadanes_algorithm import kadanes_algorithm


def test_case_1_one_number():
    arr = [12]
    assert 12 == kadanes_algorithm(arr)


def test_case_2_only_positive():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert 55 == kadanes_algorithm(arr)


def test_case_3_one_number_negative():
    arr = [-1]
    assert -1 == kadanes_algorithm(arr)


def test_case_4_mix_1():
    arr = [1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]
    assert 35 == kadanes_algorithm(arr)


def test_case_2_mix():
    arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    assert 19 == kadanes_algorithm(arr)


def test_case_3_mix():
    arr = [3, 4, -6, 7, 8, -18, 100]
    assert 100 == kadanes_algorithm(arr)
