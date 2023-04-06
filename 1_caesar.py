from typing import Iterable, Callable, Tuple

TextAlgo = Callable[[str], Iterable[str]]

def caesar(domain: str, key: int) -> Tuple[TextAlgo, TextAlgo]:
    # функція створює шифрувальну та дешифрувальну функції

    def enc(text: str) -> Iterable[str]:
        def enc_char(ch: str) -> str:
            try:
                code = domain.index(ch)
            except ValueError:
                raise ValueError(f'Character {ch} (`{ord(ch)=}`) is not in domain')
            enc = (code + key) % len(domain)
            return domain[enc]
        # символи тексту шифруються по одному й повертаються у вигляді генератора
        return map(enc_char, text)

    def dec(enc_text: str) -> Iterable[str]:
        def dec_char(ch: str) -> str:
            try:
                enc_code = domain.index(ch)
            except ValueError:
                raise ValueError(f'Character {ch} (`{ord(ch)=}`) is not in domain')
            dec = (enc_code - key) % len(domain)
            return domain[dec]
        # символи шифротексту дешифруються по одному й повертаються у вигляді генератора
        return map(dec_char, enc_text)

    return enc, dec

if __name__ == '__main__':
    # номер в журналі
    order = 14
    key = (order + 1) % 17

    # алфавіт
    domain = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

    encryptor, decryptor = caesar(domain, key)
    text = 'КРИПТОГРАФІЯ'
    enc_text = ''.join(encryptor(text))
    dec_text = ''.join(decryptor(enc_text))
    print('`', text, '` -> `', enc_text, '` -> `', dec_text, '`', sep='')

