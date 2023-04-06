from typing import Tuple

def ext_euclid(a: int, b: int) -> Tuple[int, int, int]:
    ''' Solve ax + by = GCD(a, b) for x and y and find GCD(a, b) '''
    if b == 0:
        return 1, 0
    x, y = ext_euclid(b, a % b)
    return y, x - a // b * y

if __name__ == '__main__':
    a = 2
    b = 11
    print('(x, y) =', ext_euclid(a, b))
