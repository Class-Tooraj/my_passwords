###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT
import random

# IMPORT NESTED CIPHER
import nested_cipher

# TYPE IMPORT
from typing import Iterable, Iterator


# KEY
def key_maker(length: int = None, chars: str = None, skip: Iterable[str] = None) -> str:
    """[Key Maker Function]

    Args:
        length (int, optional): [Make Key Length]. Defaults to '32'.
        chars (str, optional): [Characters For Key Make]. Defaults to 'Ascii 32:126'.
        skip (Iterable[str], optional): [Skip Characters]. Defaults to None.

    Returns:
        str: [Created Key]
    """
    chars = "".join([chr(i) for i in range(32, 127)]) if chars is None else chars
    length = 32 if length is None else length

    if skip:
        for i in skip:
            chars = chars.replace(i, '')

    _len = len(chars)
    _idx = (chars[random.randint(0, _len)] for _ in range(0, length))

    return ''.join(iter(_idx))

# CRYPTO
def crypto(text: str, key: str) -> str:
    """[Crypto XOR String]

    Args:
        text (str): [Text for Encrypt Or Decrypt]
        key (str): [Key Crypto]

    Returns:
        str: [Encrypt string or Decrypt string]
    """

    def str_key(key: str, end: int) -> Iterator:
        """[Inner Function Key Iter]

        Args:
            key (str): [Key Crypt]
            end (int): [Need How Many]

        Yields:
            Iterator: [unicode id key]
        """
        _len_key = len(key)
        _idx = 0

        for _ in range(0, end):

            if _idx == _len_key:
                _idx = 1
                key = ''.join(reversed(key))
                yield ord(key[0])
            
            else:
                yield ord(key[_idx])
                _idx += 1

    def str_xor(inp: str, key: str) -> Iterator:
        """[Inner Function Xor String]

        Args:
            inp (str): [Text For Encrypt or Decrypt]
            key (str): [Key]

        Yields:
            Iterator: [Character Encrypt or Decrypt]
        """
        xor = lambda a, b: ord(a) ^ b
        key = str_key(key, len(inp))

        for c in inp:
            yield chr(xor(c, next(key)))

    xor = str_xor(text, key)
    return ''.join(xor)

# CIPHER STRING DATA
class Cipher:
    __METHODS: tuple[str, ...] = ('b64','ab64','mb64','eb64','lb64','rb64','rab64','rmb64','reb64','rlb64')

    def __init__(self, key: str = None, method: str = None, cipher_key: bool = True) -> None:
        if method is not None:
            if method not in self.__METHODS:
                raise NameError(f'Method Name is Wrongs! All Method Supports \n\t{self.__METHODS}')

        if key is None:
            self.__key = False
        else:
            self.__key = self.cipher_encode('mb64', key) if cipher_key is True else key

        self.__cipher = "rmb64" if method is None else method

        self.gen_key = lambda length: key_maker(length= length, skip = "*+/\\=-_%$#@!~.?:;'\"{[|]}^&(),`")
        self.method_active = lambda : self.__cipher
        self.all_method_supports = lambda : ' - '.join(self.__METHODS)

    def update_method(self, method: str) -> None:
        if method not in self.__METHODS:
            raise NameError(f'Method Name is Wrongs! All Method Supports \n\t{self.__METHODS}')
        self.__cipher = method

    def update_key(self, key: str, cipher_key: bool = True) -> None:
        self.__key = self.cipher_encode('mb64', key) if cipher_key is True else key

    def encode(self, inp: str) -> str:
        inp = self.__crypt(inp, self.__key)
        return self.cipher_encode(self.__cipher, inp)

    def decode(self, inp: str) -> str:
        inp = self.cipher_decode(self.__cipher, inp)
        return self.__crypt(inp, self.__key)

    @ staticmethod
    def cipher_encode(ci: str, inp: str) -> str:
        ex = f"nested_cipher.{ci}_encode"
        ex = eval(ex)
        return ex(inp.encode('utf-8')).decode('ascii')

    @ staticmethod
    def cipher_decode(ci: str, inp: str) -> str:
        ex = f"nested_cipher.{ci}_decode"
        ex = eval(ex)
        return ex(inp.encode('ascii')).decode('utf-8')

    @ staticmethod
    def __crypt(t: str, k: str) -> str:
        return crypto(t, k)

