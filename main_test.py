import random
import main


def test_mylabmda1():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('test list data', numbers)
    result = main.mylambda1(numbers, main.collectOddElm)
    print('Your output for length: ', result)
    assert result == 5, "Invalid value. Expected 5"


def test_makeLabmda2():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('test list data', numbers)
    result = main.mylambda2(numbers, main.collectOddElm)
    print('Your output for max: ', result)
    assert result == 9, "Invalid value. Expected 9"
