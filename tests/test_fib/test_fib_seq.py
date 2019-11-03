import pytest

from fib import fib_seq

def test_fib_seq_arg_negative():
    with pytest.raises(ValueError):
        _ = fib_seq(-1)

@pytest.mark.parametrize("n", [
    5.0,
    "2",
    8j,
    [7],
    (3,),
])
def test_fib_seq_arg_wrong_type(n):
    with pytest.raises(TypeError):
        _ = fib_seq(n)

@pytest.mark.parametrize("n,expected", [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (4, [0, 1, 1, 2]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    (20, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
        1597, 2584, 4181]),
])
def test_fib_seq(n, expected):
    assert list(fib_seq(n)) == expected
