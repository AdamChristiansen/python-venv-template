from collections.abc import Iterable
from itertools import product
import pytest

import fib

def flat_prod(*xs):
    # itertools.chain cannot be used for flattening because it cannot handle
    # functions as elements
    fs = []
    for ps in product(*xs):
        fp = []
        for p in ps:
            if isinstance(p, Iterable):
                fp.extend(p)
            else:
                fp.append(p)
        fs.append(fp)
    return fs

FIB_FUNCS = [
    fib.fib,
    fib.fib_approx,
    fib.fib_dp,
    fib.fib_memo,
    fib.fib_rec,
]

@pytest.mark.parametrize("fib_func", FIB_FUNCS)
def test_fib_approx_arg_negative(fib_func):
    with pytest.raises(ValueError):
        _ = fib_func(-1)

@pytest.mark.parametrize("fib_func,n", product(FIB_FUNCS, [
    None,
    5.0,
    "2",
    8j,
    [7],
    (3,),
]))
def test_fib_approx_arg_wrong_type(fib_func, n):
    with pytest.raises(TypeError):
        _ = fib_func(n)

@pytest.mark.parametrize("fib_func,n,expected", flat_prod(FIB_FUNCS, [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (20, 6765),
]))
def test_approx_rec(fib_func, n, expected):
    assert fib_func(n) == expected
