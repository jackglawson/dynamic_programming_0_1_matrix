import numpy as np

SIZE = 12
zero = 'o'
one = 'x'
empty = '.'


def cache(func):
    d = {}

    def wrapper(c):
        e = encode(c)
        try:
            result = d[e]
        except KeyError:
            result = func(c)
            d[e] = result
        return result

    return wrapper


def encode(c):
    """
    Candidates are encoded before being saved in the cache.
    This allows us to exploit symmetry between unsolved grids.
    We exploit two symmetries:
    1. The order of elements in the column above an element does not matter for the element. Only the number of ones and
    zeroes yet to be placed in that column matters
    2. The order of the columns themselves does not matter
    """
    num_0s_to_be_placed = SIZE / 2 - np.count_nonzero(c == zero, axis=0)
    num_1s_to_be_placed = SIZE / 2 - np.count_nonzero(c == one, axis=0)
    return tuple(sorted(zip(num_0s_to_be_placed, num_1s_to_be_placed)))


@cache
def bt(c):
    """backtracking algorithm, with caching for dynamic programming
    If we get to an incomplete grid that has symmetry with a previous incomplete grid, we already know how many
    solutions it's going to lead to"""

    count = 0

    if reject(c):
        return 0
    if accept(c):
        return 1

    # we fill the grid from left to right, then from top to bottom
    first_empty = find_first_empty(c)
    for possibility in [zero, one]:
        c[first_empty] = possibility
        count += bt(c)
        c[first_empty] = empty

    return count


def root():
    """the root of the backtracking tree"""
    root = np.ndarray((SIZE, SIZE), dtype='<U1')
    root[:] = '.'
    return root


def reject(c):
    """return true only if the partial candidate c is not worth completing"""
    if (np.any(np.count_nonzero(c == zero, axis=0) > SIZE / 2)
            or np.any(np.count_nonzero(c == zero, axis=1) > SIZE / 2)
            or np.any(np.count_nonzero(c == one, axis=0) > SIZE / 2)
            or np.any(np.count_nonzero(c == one, axis=1) > SIZE / 2)):
        return True

    else:
        return False


def accept(c):
    """return true if c is a solution of P, and false otherwise"""
    if (np.all(np.count_nonzero(c == zero, axis=0) == SIZE / 2)
            and np.all(np.count_nonzero(c == zero, axis=1) == SIZE / 2)
            and np.all(np.count_nonzero(c == one, axis=0) == SIZE / 2)
            and np.all(np.count_nonzero(c == one, axis=1) == SIZE / 2)):
        return True

    else:
        return False


def find_first_empty(c):
    """find the coords of the first empty space"""
    for row in range(SIZE):
        for col in range(SIZE):
            if c[row, col] == '.':
                return row, col


def solve():
    return bt(root())


print(solve())
