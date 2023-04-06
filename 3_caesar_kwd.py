from typing import Iterable, Callable, Tuple
import re

TextAlgo = Callable[[str], Iterable[str]]

def shift_domain(domain: str, shift: int, word: str) -> str:
    # видалення букв слова з домену
    rest = ''.join(re.split('[' + word + ']', domain))
    split = len(domain) - len(word) - shift
    return rest[split:] + word + rest[:split]

def caesar(domain: str, key: Tuple[int, str]) -> Tuple[TextAlgo, TextAlgo]:
    shift, word = key
    dom_shift = shift_domain(domain, shift, word)

    def enc(text: str) -> Iterable[str]:
        def enc_char(ch: str) -> str:
            return dom_shift[domain.index(ch)]
        return map(enc_char, text)

    def dec(enc_text: str) -> Iterable[str]:
        def dec_char(ch: str) -> str:
            return domain[dom_shift.index(ch)]
        return map(dec_char, enc_text)

    return enc, dec

if __name__ == '__main__':
    domain = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    key = 5, 'ФОРЕЛЬ'
    encryptor, decryptor = caesar(domain, key)

    text = 'ШКОЛА'
    enc_text = ''.join(encryptor(text))
    dec_text = ''.join(decryptor(enc_text))
    print('`', text, '` -> `', enc_text, '` -> `', dec_text, '`', sep='')
