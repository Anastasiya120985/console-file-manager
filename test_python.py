def test_filter():
    assert list(filter(lambda x: x > 4, [1, 2.0, 3.1, 4, 5, 6, 7.9])) == [5, 6, 7.9]
    assert list(filter(lambda x: type(x) is int, [1, 2.0, 3.1, 4, 5, 6, 7.9])) == [1, 4, 5, 6]
    assert list(filter(lambda x: '.' in x, ['ноль', '1', '2.0', '3.1', '4', '5', '7.9', 'семь'])) == ['2.0', '3.1', '7.9']
def test_map():
    assert list(map(int, ['4', '5', '9'])) == [4, 5, 9]
    assert list(map(abs, [-2, -1, 0, 1, 2])) == [2, 1, 0, 1, 2]
    assert list(map(len, ["Welcome", "to", "Real", "Python"])) == [7, 2, 4, 6]
def test_sorted():
    assert sorted({2: 'red', 1: 'green', 3: 'blue'}) == [1, 2, 3]
    assert sorted("hello") == ['e', 'h', 'l', 'l', 'o']
    assert sorted([1, 4, 5, 2, 456, 12]) == [1, 2, 4, 5, 12, 456]

import math
def test_pi():
    assert math.pi == 3.141592653589793
    assert math.pi * (2 ** 2) == 12.566370614359172
def test_sqrt():
    assert math.sqrt(81) == 9.0
    assert math.sqrt(9) == 3.0
def test_pow():
    assert math.pow(3, 4) == 81.0
    assert math.pow(5, 6) == 15625.0
def test_hypot():
    assert math.hypot(3, 2) == 3.605551275463989
    assert math.hypot(-3, 3) == 4.242640687119285
    assert math.hypot(0, 2) == 2.0
