from typing import Callable, Sequence, Iterable, Tuple

def notepad(key: Sequence[int]) -> Tuple[Callable[[str], Iterable[int]], \
                                         Callable[[Sequence[int]], str]]:
    def enc(text: str) -> Iterable[int]:
        if len(text) != len(key):
            raise ValueError('Different lengths of text and key')
        def enc_char(ch: str, code: int) -> int:
            return ord(ch) ^ code
        return map(enc_char, text, key)

    def dec(enc_text: Sequence[int]) -> str:
        if len(enc_text) != len(key):
            raise ValueError('Different lengths of encrypted text and key')
        def dec_char(enc_ch: int, code: int) -> str:
            return chr(enc_ch ^ code)
        return map(dec_char, enc_text, key)

    return enc, dec

if __name__ == '__main__':
    key = 0b110000, 0b011110, 0b010100
    encryptor, decryptor = notepad(key)
    text = 'Eduard'[:3]

    enc_text = tuple(encryptor(text))
    dec_text = ''.join(decryptor(enc_text))
    print('`', text, '` -> `', tuple(map(bin, enc_text)), '` -> `', dec_text, '`', sep='')

