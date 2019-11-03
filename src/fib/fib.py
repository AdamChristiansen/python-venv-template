from math import sqrt

# This constant is the golden ratio, which is intrinsically related to the
# Fibonacci sequence.
_PHI = (sqrt(5) + 1) / 2

def fib_rec(n):
    """
    The standard recursive definition of the Fibonacci sequence to find a
    single Fibonacci number . It runs in O(2 ** n) time with O(1) space
    complexity (or O(n) if stack space is considered).
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_memo(n, memo=None):
    """
    The standard recursive definition of the Fibonacci sequence to find a
    single Fibonacci number but improved using a memoization technique to
    minimize the number of recursive calls. It runs in O(n) time with O(n)
    space complexity.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    elif memo is None:
        memo = {}
    elif n in memo:
        return memo[n]
    f0 = memo[n - 1] if n - 1 in memo else fib_memo(n - 1, memo)
    f1 = memo[n - 2] if n - 2 in memo else fib_memo(n - 2, memo)
    memo[n] = f0 + f1
    return memo[n]


def fib_dp(n):
    """
    An optimized dynamic programming solution to find a single number of the
    Fibonacci sequence. It runs in O(n) time with O(1) space complexity.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    f0, f1 = 0, 1
    for _ in range(n):
        f0, f1 = f1, f0 + f1
    return f0


def fib_approx(n):
    """
    A constant time approximation for a single number of the Fibonacci
    sequence. This decreases in accuracy as `n` increases. It runs in O(1)
    time with O(1) space complexity.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    return round(_PHI ** n / sqrt(5))

def fib(n):
    """
    The fastest algorithm to compute a single number of the Fibonacci sequence
    that is always correct.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    return fib_dp(n)

class fib_seq:
    """
    A generator that yields numbers of the Fibonacci sequence. If no argument
    is supplied it will generate forever, but an optional exclusive bound can
    be supplied to generate the first `n` numbers of the sequence.
    """

    def __init__(self, n=None):
        if not isinstance(n, (int, type(None))):
            raise TypeError("n must be an int or None")
        if n is not None and n < 0:
            raise ValueError("n must be non-negative")
        self._n = n

    def __iter__(self):
        self._c = 0
        self._f0 = 0
        self._f1 = 1
        return self

    def __next__(self):
        if self._n is not None and self._c >= self._n:
            raise StopIteration
        f = self._f0
        self._f0, self._f1 = self._f1, self._f0 + self._f1
        self._c += 1
        return f
