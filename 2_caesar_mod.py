from typing import Iterable, Callable, Tuple
from math import gcd

TextAlgo = Callable[[str], Iterable[str]]

def caesar(domain: str, key: Tuple[int, int]) -> Tuple[TextAlgo, TextAlgo]:
    a, b = key
    m = len(domain)
    if gcd(a, m) != 1:
        raise ValueError('GCD({a=}, {m=}) != 1')

    def enc(text: str) -> Iterable[str]:
        def enc_char(ch: str) -> str:
            t = domain.index(ch)
            enc = (a * t + b) % m
            return domain[enc]
        return map(enc_char, text)

    def dec(enc_text: str) -> Iterable[str]:
        def dec_char(ch: str) -> str:
            enc = domain.index(ch)
            dec_part = (enc - b) % m
            # dec підбирається, оскільки точне значення dec одразу віднайти неможливо
            # через неін'єктивність операції mod
            while dec_part / a != (dec := int(dec_part / a)):
                dec_part += m
            return domain[dec]
        return map(dec_char, enc_text)

    return enc, dec

if __name__ == '__main__':
    # алфавіт
    domain = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

    key = 7, 14

    encryptor, decryptor = caesar(domain, key)
    text = 'КРИПТОГРАФІЯ'
    enc_text = ''.join(encryptor(text))
    dec_text = ''.join(decryptor(enc_text))
    print('`', text, '` -> `', enc_text, '` -> `', dec_text, '`', sep='')
