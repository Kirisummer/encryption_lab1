from typing import Iterable, Callable, Tuple
from itertools import cycle

TextAlgo = Callable[[str], Iterable[str]]

def vigenere(domain: str, key: str) -> Tuple[TextAlgo, TextAlgo]:
    def enc(text: str) -> Iterable[str]:
        m = len(domain)
        def enc_char(ch: int, shift: int) -> str:
            return domain[(ch + shift) % m]
        return map(enc_char,
                   map(domain.index, text), # символи тесту переводяться до індексів
                   cycle(map(domain.index, key)) # символи ключа переводяться до індексів
        )                                        # й нескінченно повторюються

    def dec(enc_text: str) -> Iterable[str]:
        m = len(domain)
        def dec_char(enc_ch: int, code: int) -> str:
            return domain[(enc_ch + m - code) % m]
        return map(dec_char,
                   map(domain.index, enc_text),
                   cycle(map(domain.index, key))
        )

    return enc, dec

if __name__ == '__main__':
    domain = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ '
    key = 'ЯКОР'

    encryptor, decryptor = vigenere(domain, key)
    text = 'ОСТАННЯ НАДІЯ'
    enc_text = ''.join(encryptor(text))
    dec_text = ''.join(decryptor(enc_text))
    print('`', text, '` -> `', enc_text, '` -> `', dec_text, '`', sep='')
    
