from typing import Iterable, Callable, Tuple, Sequence, Any
from itertools import islice

TextAlgo = Callable[[str], Iterable[str]]

# Матриці #####################################################################

Vector = Sequence[int]
Matrix = Sequence[Vector]

def mult(matrix: Matrix, vector: Vector, modulo: int) -> Vector:
    def mult_vect(row: Vector):
        if len(row) != len(vector):
            raise ValueError(f'Different length: {len(row)} vs {len(vector)}')
        return sum(map(int.__mul__, row, vector)) % modulo
    return tuple(map(mult_vect, matrix))

# Не матриці ##################################################################

def batched(it: Iterable, n: int):
    it = iter(it)
    while batch := tuple(islice(it, n)):
        yield batch

def hill(domain: str, key: Matrix) -> Tuple[TextAlgo, TextAlgo]:
    def enc(text: str) -> Iterable[str]:
        for block in batched(text, len(key[0])):
            vector = tuple(domain.index(ch) for ch in block)
            enc_block = mult(key, vector, len(domain))
            yield from map(domain.__getitem__, enc_block)

    def dec(text: str) -> Iterable[str]:
        pass

    return enc, dec

if __name__ == '__main__':
    domain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    key = ((3, 1), (6, 5))

    encryptor, decryptor = hill(domain, key)
    text = 'BUSINESS IS BUSINESS'
    enc_text = ''.join(encryptor(text))
    print('`', text, '` -> `', enc_text, sep='')
    

