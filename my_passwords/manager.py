###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT
import os
import sqlite3
import random
import hashlib

from datetime import datetime

# IMPORT NESTED CIPHER
import nested_cipher

# TYPE IMPORT
from typing import Callable, Iterable, Iterator

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
        skip = set(skip)
        chars = set(chars).difference(skip)
        chars = ''.join(chars)

    _idx = (random.choice(chars) for _ in range(0, length))

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
    """[Cipher String Data]
    Simply Encode or Decode and Encrypt or Decrypt String

    Raises:
        init:
            NameError: [Method Name If Not Exists]
        update_method:
            NameError: [Method Name If Not Exists]
    """
    VERSION: str = "0.1"

    __METHODS: tuple[str, ...] = ('b64','ab64','mb64','eb64','lb64','rb64','rab64','rmb64','reb64','rlb64')

    def __init__(self, key: str = None, method: str = None, cipher_key: bool = True) -> None:
        """[Initialize Cipher]

        Args:
            key (str, optional): [Crypto Key]. Defaults to None. 'None' mean only cipher.
            method (str, optional): [Cipher Method]. Defaults to None. 'None' mean rmb64.
            cipher_key (bool, optional): [Cipher Key]. Defaults to True. 'True' mean key to cipher key.

        Raises:
            NameError: [Method Name If Not Exist]
        """
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
        """[Update Cipher Method]

        Args:
            method (str): [Chose Method]

        Raises:
            NameError: [Method Name If Not Exist]
        """
        if method not in self.__METHODS:
            raise NameError(f'Method Name is Wrongs! All Method Supports \n\t{self.__METHODS}')
        self.__cipher = method

    def update_key(self, key: str, cipher_key: bool = True) -> None:
        """[Update Crypto Key]

        Args:
            key (str): [Key]
            cipher_key (bool, optional): [Cipher Key]. Defaults to True. 'True' mean key to cipher key.
        """
        self.__key = self.cipher_encode('mb64', key) if cipher_key is True else key

    def encode(self, inp: str) -> str:
        """[Encode - Cipher or Encrypt and Cipher]

        Args:
            inp (str): [input string]

        Returns:
            str: [encoded string]
        """
        if self.__key:
            inp = self.__crypt(inp, self.__key)
        return self.cipher_encode(self.__cipher, inp)

    def decode(self, inp: str) -> str:
        """[Decode - Cipher or Cipher and Decrypt]

        Args:
            inp (str): [input Cipher]

        Returns:
            str: [source string]
        """
        inp = self.cipher_decode(self.__cipher, inp)
        return self.__crypt(inp, self.__key) if self.__key is not False else inp

    @ staticmethod
    def cipher_encode(ci: str, inp: str) -> str:
        """[Cipher Encoder]

        Args:
            ci (str): [method name]
            inp (str): [input string]

        Returns:
            str: [encoded string]
        """
        ex = f"nested_cipher.{ci}_encode"
        ex = eval(ex)
        return ex(inp.encode('utf-8')).decode('ascii')

    @ staticmethod
    def cipher_decode(ci: str, inp: str) -> str:
        """[Cipher Decoder]

        Args:
            ci (str): [method name]
            inp (str): [input cipher]

        Returns:
            str: [source string]
        """
        ex = f"nested_cipher.{ci}_decode"
        ex = eval(ex)
        return ex(inp.encode('ascii')).decode('utf-8')

    @ staticmethod
    def __crypt(txt: str, key: str) -> str:
        """[Encrypt or Decrypt]

        Args:
            txt (str): [String]
            key (str): [Key]

        Returns:
            str: [Encrypt Or Decrypt String]
        """
        return crypto(txt, key)

# MANAGER
class Manager:
    """[Simple Password Manager]
    Use Sqlite3 Data Base
    """
    VERSION: str = "0.2"

    NOW: Callable = lambda _: datetime.now()
    HASH: Callable = lambda _,x: hashlib.sha256(x) if isinstance(x, bytes) else hashlib.sha256(x.encode('utf-8'))
    METHOD: str = 'rmb64'

    def __init__(self, path: str, user_name: str, password: str) -> None:
        """[Initialize]

        Args:
            path (str): [Data Base Path]
            user_name (str): [UserName]
            password (str): [Password]

        Raises:
            Sqlite_ERROR: [Data Base Error]
        """
        self.__path = os.path.realpath(path) if path != ':memory:' else path
        if user_name == password:
            print("ACCOUNT ERR --> 'USER_NAME' and 'PASSWORD' should not be the same !")
            exit()

        if len(password) < 6:
            print("ACCOUNT ERR --> 'PASSWORD' length must be at least '6' characters !")
            exit()

        password = self.HASH(password).hexdigest()
        self.__account = (user_name, password)

        try:
            self.__db = sqlite3.connect(self.__path)
        except (sqlite3.Error, BaseException) as err:
            raise err

        self.__commit = self.__db.commit
        self.__cipher = Cipher(crypto(password, user_name), self.METHOD)
        self.__initialize()

        if self.__init_data:
            safe_key = crypto(self.__init_data['KEY'][0], password)
            self.__cipher.update_key(safe_key)
        else:
            print("ACCOUNT_ERROR --> 'USER_NAME' or 'PASSWORD' is 'WRONG' !!")
            exit()

    def __initialize(self) -> int:
        """
        Initialize Data Check if First Run or Data Base Is First Run
        Other Get Init Data From Data Base
        """
        tbl_app = """CREATE TABLE IF NOT EXISTS App (
                                    id integer PRIMARY KEY,
                                    Name text NOT NULL,
                                    Data text NOT NULL,
                                    LastUpdate timestamp
                                    );"""
        tbl_pass = """CREATE TABLE IF NOT EXISTS Password (
                                    id integer PRIMARY KEY,
                                    Name text NOT NULL,
                                    Password text NOT NULL,
                                    URL text,
                                    More text,
                                    SetTime timestamp NOT NULL,
                                    LastUpdate timestamp
                                    );"""

        c_script = "SELECT name FROM sqlite_master WHERE type='table' AND name= ?;"
        check = [
            len(self.__db.execute(c_script, ('App',)).fetchall()) > 0,
            len(self.__db.execute(c_script, ('Password',)).fetchall()) > 0,
        ]
        if all(check):
            init_data = self.__db.execute("SELECT Data FROM 'App' WHERE (name= ?)", ('init',)).fetchone()[0]
            init_data = self.__cipher.decode(init_data)
            if self.__account[0] in init_data:
                self.__init_data = eval(init_data)
                return 0
            else:
                self.__init_data = None
                return -1
        else:
            _key: str = key_maker(64)
            _key: str = crypto(_key, self.__account[1])
            init_data = {
                self.__account[0]: self.__account[1], 
                'KEY': [_key]
            }

            init_data = self.__cipher.encode(format(init_data))
            self.__db.execute(tbl_app)
            self.__db.execute(tbl_pass)

            self.__db.execute("INSERT INTO App VALUES(?,?,?,?)", (0, 'init', init_data, self.NOW()))
            self.__commit()

            self.__initialize()

            return 1

    def last_id(self, table: str) -> int:
        """[Last ID From Table]

        Args:
            table (str): [Table Name]

        Returns:
            int: [Maximum ID Exists in Table]
        """
        max_id = self.__db.execute(f'SELECT max(id) FROM {table}').fetchone()[0]
        if max_id is None:
            return 0
        return max_id

    def exists(self, name: str) -> bool:
        """[Exists Name In Data Base]

        Args:
            name (str): [Name For Check]

        Returns:
            bool: [If Exists True Else False]
        """
        get = self.__db.execute(f"SELECT * FROM 'Password' WHERE (Name= ?)", (name,)).fetchall()
        return True if len(get) > 0 else False

    def add_pass(self, name: str, password: str, url: str = None, more: str = None) -> bool:
        """[Add Password In data Base]

        Args:
            name (str): [Name Password]
            password (str): [Password]
            url (str, optional): [URL or Account or other txt | Optional]. Defaults to None.
            more (str, optional): [More Detail or Info | Optional]. Defaults to None.

        Returns:
            bool: [If Set To db True Else False]
        """
        if not self.exists(name):
            _id = self.last_id('Password') + 1
            url = '' if url is None else self.__cipher.encode(url)
            more = '' if more is None else self.__cipher.encode(more)
            password = self.__cipher.encode(password)
            now = self.NOW()
            data = (_id, name, password, url, more, now, now)
            self.__db.execute("INSERT INTO Password VALUES(?,?,?,?,?,?,?)", data)
            self.__commit()
            return True
        else:
            return False

    def get_pass(self, name: str, ret: str = 'all') -> str:
        """[Get Password From Data Base]

        Args:
            name (str): [Name Password]
            ret (str, optional): [Return Data]. Defaults to 'all'.
                ret :: 'all, id, name, password, url, more, settime, lastupdate'
                Example ret : 'id, name, password'
        Returns:
            str: [String Result]
        """
        _ret = {
            'all': '-A-', 'id': 'id', 'name': 'Name', 'password': 'Password', 'url': 'URL', 'more': 'More', 'settime': 'SetTime', 'lastupdate': 'LastUpdate'
            }
        idx_name = ['id', 'Name', 'Password', 'URL', 'More', 'SetTime', 'LastUpdate']
        ret = _ret[ret.lower()] if ',' not in ret else [_ret[i.lower()] for i in ret.split(',')]

        get = self.__db.execute(f"SELECT * FROM 'Password' WHERE (Name= ?)", (name,)).fetchone()
        result = {}
        for n, i in enumerate(get):
            if 1 < n < 5 and i != '':
                result[idx_name[n]] = self.__cipher.decode(i)
            else:
                if i == '':
                    result[idx_name[n]] = 'None'
                else:
                    result[idx_name[n]] = i
        if ret != '-A-':
            return ','.join([result[i] for i in ret]) if isinstance(ret, list) else result[ret]
        else:
            return ','.join(str(i) for i in result.values())

    def update_pass(self, name: str, password: str = None, url: str = None, more: str = None) -> bool:
        """
        [Update or Replace Data In data Base]

        Args:
            name (str): [Name Password]
            password (str, optional): [Password]. Defaults to None.
            url (str, optional): [URL or Account or other txt | Optional]. Defaults to None.
            more (str, optional): [More Detail or Info | Optional]. Defaults to None.

        Returns:
            bool: [If Set To db True Else False]
        """
        enc = self.__cipher.encode
        scr = """
            UPDATE OR REPLACE Password
            SET Password=:password, URL=:url, More=:more, LastUpdate=:lu
            WHERE id=:id and Name=:name;
            """
        if self.exists(name):
            get = self.__db.execute(f"SELECT * FROM 'Password' WHERE (Name= ?)", (name,)).fetchone()
            upd = {
                'id': get[0],
                'name': get[1],
                'password': enc(password) if password is not None else get[2],
                'url': enc(url) if url is not None else get[3],
                'more': enc(more) if more is not None else get[4],
                'lu': self.NOW(),
            }
            self.__db.execute(scr, upd)
            self.__commit()
            return True
        return False

    def del_pass(self, name: str, secure: bool = True) -> bool:
        """[Delete Password]

        Args:
            name (str): [Name For Delete Row]
            secure (bool, optional): [Secure replace Data With Random Data First And Then Delete]. Defaults to True.
        Returns:
            bool: [If Deleted True Else False]
        """
        if not self.exists(name):
            return False
        if secure:
            self.update_pass(name, key_maker(32), key_maker(10), key_maker(20))
            self.__commit()

        _id, = self.__db.execute("SELECT id FROM Password WHERE (Name= ?)", (name,)).fetchone()

        self.__db.execute("DELETE FROM Password WHERE id= ? and Name= ?", (_id, name))
        self.__commit()

        return True if not self.exists(name) else False

    def counter_password(self) -> int:
        """[Conter Password]

        Returns:
            int: [How Many Row In Password Table]
        """
        return self.__db.execute("SELECT COUNT(*) FROM Password").fetchone()[0]

    def reset(self, mode: int = 1) -> bool:
        """[Reset Data Base]

        Args:
            mode (int, optional): [Reset Mode Valid (1, 2)]. Defaults to 1.
                mode 1 : Delete All Password And Clear Table
                mode 2 : Delete All Data From Data Base And Remove Data Base file

        Returns:
            bool: [True If Not is Wrong Else False]
        """
        modes = (1, 2)
        if mode == 1:
            try:
                self.__db.execute("DELETE FROM 'Password';")
                self.__commit()

                return True if self.counter_password() == 0 else False
            except (BaseException, Exception) as err:
                print(f"{err}")
                return False

        elif mode == 2:
            rs_pass = self.reset(1)
            if rs_pass is True:
                try:
                    self.__db.execute("DELETE FROM 'App';")
                    self.__commit()
                    self.__db.close()

                    if self.__path != ":memory:":
                        os.remove(self.__path)
                    return True
                except (BaseException, Exception, FileExistsError, FileNotFoundError) as err:
                    print(f"{err}")
                    return False
            else:
                return False
        else:
            print(f"Mode {mode} is Not Exists - Chose {modes}")
            return False
    
    def get_all_name(self) -> Iterable:
        return (i[0] for i in self.__db.execute("SELECT name FROM Password").fetchall())

    def close(self) -> None:
        """[Close]
        """
        self.__path = None
        self.__account = None
        self.__cipher = None
        self.__init_data = None
        self.__db.close()
        self.__db = None
        self.__commit = None


# USER NAME OR PASSWORD CHANGER
def account_update(path: str, old_username: str, old_password: str, new_username: str, new_password: str) -> tuple[bool, str]:
    """[Update User Name Or Password]
    Manager DataBase is Encrypted All Data With Generated Key Xor By UserName And Password
    Update Account Make New DataBase And Add All Password One By One Decrypted and New Crypting
    And Replace Old DataBase With New DataBase
    This Progres is Slow

    Args:
        path (str): [DataBase Path]
        old_username (str): [UserName]
        old_password (str): [Password]
        new_username (str): [New UserName]
        new_password (str): [New Password]

    Returns:
        tuple[bool, str]: [return bool and string details]
    """
    if old_password == new_password:
        return False, 'NewPassword is OldPassword !'

    r_path = os.path.realpath(path)
    l_path = os.path.split(r_path)
    new_path = os.path.join(l_path[0], 'acu.tm')

    _old_man = Manager(path, old_username, old_password)
    count_passwords: int = _old_man.counter_password()
    def _old_db(man: Manager) -> Iterator:
        read_db = man.get_all_name()
        for i in read_db:
            yield man.get_pass(i, 'name,password,url,more')
        man.close()
    read_old_db = _old_db(_old_man)
    del _old_man

    new_db = Manager(new_path, new_username, new_password)
    add_new = (new_db.add_pass(*i.split(',')) for i in read_old_db)
    pr: int = 16 if count_passwords >= 60 else 4
    progres: tuple[str, int] = (':', abs(count_passwords // pr))
    count = 0

    print('|', end='', flush=True)
    for _ in add_new:
        count += 1
        if count == progres[-1]:
            print(':', end='', flush=True)
            count = 0

    _add_counter  = new_db.counter_password()
    _res = f'ALL {count_passwords} - ADD {_add_counter}'
    new_db.close()
    os.remove(r_path)
    os.rename(new_path, r_path)
    print('| - 100% |DONE', flush=True)
    return (True, _res) if _add_counter == count_passwords else (False, _res)


__dir__ = ('key_maker', 'crypto', 'Cipher', 'Manager', 'account_update')
