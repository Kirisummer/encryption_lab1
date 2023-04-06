from typing import Iterable, Callable, Tuple, Sequence
from itertools import cycle

TextAlgo = Callable[[str], Iterable[str]]

def gronsfeld(domain: str, key: Sequence[int]) -> Tuple[TextAlgo, TextAlgo]:
    def enc(text: str) -> Iterable[str]:
        m = len(domain)
        def enc_char(ch: int, shift: int) -> str:
            return domain[(ch + shift) % m]
        return map(enc_char,
                   map(domain.index, text), # символи тесту переводяться до індексів
                   cycle(key)
        )

    def dec(enc_text: str) -> Iterable[str]:
        m = len(domain)
        def dec_char(enc_ch: int, shift: int) -> str:
            return domain[(enc_ch + m - shift) % m]
        return map(dec_char,
                   map(domain.index, enc_text),
                   cycle(key)
        )

    return enc, dec

if __name__ == '__main__':
    domain = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ '
    key = tuple(map(int, str(15148 - 16 * 14)))

    encryptor, decryptor = gronsfeld(domain, key)
    text = 'ОСТАННЯ НАДІЯ'
    enc_text = ''.join(encryptor(text))
    dec_text = ''.join(decryptor(enc_text))
    print('`', text, '` -> `', enc_text, '` -> `', dec_text, '`', sep='')
    

