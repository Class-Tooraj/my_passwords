###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT
import os
import json

from typing import Callable

# IMPORT MY PASSWORD
import my_passwords


# CODE

_CLEANER: str = 'clear' if os.name == 'posix' else 'cls'
_CLEAR: Callable = lambda : os.system(_CLEANER)


# SETTING
class Setting:
    VERSION: str = '0.1'

    ERROR: str = None
    __DATA: dict = None

    def __init__(self, path: str, key: str = None, method: str = 'mb64') -> None:
        self.__file = os.path.realpath(path)
        self.__DATA = {}
        if key:
            self.__cipher: my_passwords.Cipher = my_passwords.Cipher(key, method)
        else:
            self.__cipher = False

        self.connected = lambda : self.__file
        self.load_data()

    def load_data(self) -> bool:
        try:
            with open(self.__file, 'rb') as f:
                reader = json.load(f)
                self.__DATA = reader
            return True
        except (FileExistsError, FileNotFoundError, IOError, BaseException) as err:
            self.ERROR = f'<{type(err).__name__}::{err}>'
            return False

    def save_data(self) -> bool:
        try:
            with open(self.__file, 'w') as f:
                json.dump(self.__DATA, f,indent= 4)
            return True
        except (FileExistsError, FileNotFoundError, IOError, BaseException) as err:
            self.ERROR = f'<{type(err).__name__}::{err}>'
            return False

    def __setitem__(self, name: str, val: str) -> None:
        if self.__cipher:
            val = self.__cipher.encode(val)
        self.__DATA[name] = val

    def __getitem__(self, name: str) -> object:
        get = self.__DATA.get(name, None)
        if get is None:
            return None

        if self.__cipher:
            return self.__cipher.decode(get)

        return get

def about_info() -> str:
    _show = (
        "\tABOUT MY PASSWORDS\n",
        "\t---------------------------------------------------------",
        "\tSOURCE 'https://github.com/Class-Tooraj/my_passwords'",
        "\t---------------------------------------------------------",
        "\n",
        "\tVERSION CLI APP '0.1'",
        "\tVERSION PASSWORD MANAGER '0.2'",
        "\tVERSION CIPHER '0.1'",
        "\tVERSION KEY GENERATOR (KEY MAKER) '0.2'",
        "\tVERSION CRYPTO '0.3'",
        "\tVERSION UPDATE ACCOUNT (ACCOUNT UPDATE) '0.2'",
        "\n",
        "\t---------------------------------------------------------",
        "\tPYTHON 3 - SQLITE 3 - NESTED CIPHER 0.3",
        "\t---------------------------------------------------------",
        "\n",
        "\tAUTHOR 'TOORAJ JAHANGIRI'",
        "\tEMAIL 'toorajjahangiri@gmail.com'",
        "\n\n"
    )

    return '\n'.join(_show)

# CONSOLE APP CODE
def app_password_manager(_act_db: tuple = None) -> int:
    _CLEAR()
    print('PASSWORD MANAGER APP [VERSION 0.1]')
    _manager = my_passwords.Manager
    _menu = (
        "\n\n",
        "\t1 : 'ADD' Password.\n\t\tadd Password into The DataBase.",
        "\t2 : 'GET' Password.\n\t\tget Data From Data Base.",
        "\t3 : 'ALL NAME' Password.\n\t\tget All Name Existed into Data Base.",
        "\t4 : 'UPDATE' Password.\n\t\tupdate or replace Data.",
        "\t5 : 'EXISTS' Password.\n\t\texists data into Data Base.",
        "\t6 : 'COUNT' Password.\n\t\tcount Password into Data Base.",
        "\t7 : 'DELETE' Password.\n\t\tdelete Password From data Base.",
        "\t8 : 'RESET' Data Base.\n\t\treset DATA BASE *REMOVE ALL PASSWORD or *DELETE DATA BASE.",
        "\t0 : 'EXIT'\n\t\tQuit Application.",
        "\t-1 : 'CLEAR' Console Screen\n\t\tClear Display U can Use 'cls' or 'clear'.",
        "\n",
    )
    if _act_db is not None:
        assert len(_act_db) == 4
        _path, _method, _username, _password = _act_db
    else:
        print("... CONNECT TO DATABASE ...")
        _path = str(input('PATH /> '))
        _method = str(input('METHOD /> '))
        _username = str(input('USERNAME /> '))
        _password = str(input('PASSWORD /> '))
    _manager.METHOD = _method
    _manager = _manager(_path, _username, _password)
    _CLEAR()
    print('PASSWORD MANAGER APP [VERSION 0.1]')
    print(f'\n\t< DATA BASE [{os.path.basename(_path)}] IS ACTIVE >')
    print("\t------------------------------------------------------")
    print('\n'.join(_menu))
    _running = True
    while _running:
        _inp = str(input('-- /> '))
        _inp = int(_inp) if _inp.isdigit() else _inp.lower()
        if _inp == 0:
            print("-- CLOSING --")
            _manager.close()
            _running = False
            _CLEAR()
            break
        elif _inp == 1:
            print("ADD PASSWORD INTO DATA BASE")
            _add_run = True
            while _add_run:
                _name = str(input('NAME /> '))
                _pass = str(input('PASSWORD /> '))
                _url = str(input('URL /> '))
                _url = _url if _url not in('', ' ', None) else None
                _more = str(input('MORE /> '))
                _more = _more if _more not in('', ' ', None) else None
                _added = _manager.add_pass(_name, _pass, _url, _more)
                print(f"PASSWORD [{_name}] IS [{'ADDED' if _added is True else 'CAN NOT ADD'}]")
                _next = str(input("MORE PASSWORD ADD /> [default : 'Y'] ")).lower()
                if _next == 'n':
                    _add_run = False
                    break
            print("... ADDING PASSWORD IS DONE ...")
        elif _inp == 2:
            print("GET PASSWORD")
            _get_run = True
            while _get_run:
                _name = str(input('NAME /> '))
                _ret = str(input("GET /> [default: 'all'] "))
                _ret = 'all' if _ret in ('', ' ', None) else _ret
                _get = _manager.get_pass(_name, _ret)
                print(f"[{_name}] -> [{_get}]")
                _next = str(input("MORE GET PASSWORD /> [default : 'Y'] ")).lower()
                if _next == 'n':
                    _get_run = False
                    break
            print("... GETING PASSWORD IS DONE ...")
        elif _inp == 3:
            print("GET ALL NAME EXISTED IN DATA BASE")
            _show = str(input('SHOW /> [n: newline] or [l: line] '))
            _show = 'n' if _show in ('n', 'N', ' ', '', None) else 'l'
            _all_name = _manager.get_all_name()
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
            if _show == 'n':
                print('\n'.join(_all_name))
            else:
                print('\t'.join(_all_name))
            print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        elif _inp == 4:
            print("UPDATE OR REPLACE PASSWORD")
            _name = str(input('NAME /> '))
            _pass = str(input('PASSWORD /> '))
            _pass = _pass if _pass not in('', ' ', None) else None
            _url = str(input('URL /> '))
            _url = _url if _url not in('', ' ', None) else None
            _more = str(input('MORE /> '))
            _more = _more if _more not in('', ' ', None) else None
            _upd = _manager.update_pass(_name, _pass, _url, _more)
            print(f"[{_name}] IS [{'UPDATED' if _upd is True else 'CAN NOT UPDATE'}]")
        elif _inp == 5:
            print('EXISTED IN DATABASE')
            _name = str(input('NAME /> '))
            _ex = _manager.exists(_name)
            print(f"[{_name}] IS [{'EXISTED' if _ex is True else 'NOT EXIST'}]")
        elif _inp == 6:
            print("COUNTER PASSWORD INTO DATA BASE")
            _counter = _manager.counter_password()
            print(f"Counter Password into The Data Base : [{_counter}]")
        elif _inp == 7:
            print("DELETE PASSWORD FROM DATA BASE")
            _name = str(input('NAME /> '))
            _really = str(input(f"ARE U REALLY WANT TO REMOVE [{_name}] /> [default : 'Y'] ")).lower()
            if _really in ('y', '', ' ', None):
                _rem = _manager.del_pass(_name, secure=True)
                print(f"[{_name}] IS [{'DELETED' if _rem is True else 'NOT DELETED'}]")
            else:
                print("CANCELED BY USER")
        elif _inp == 8:
            print("RESET DATA BASE")
            print("MODE [1] : REMOVE ALL PASSWORD FROM DATA BASE\nMODE [2] : REMOVE ALL PASSWORD AND DELETE DATA BASE")
            _res = str(input('MODE /> [default "1"] '))
            _res = 1 if _res in ('', ' ', None) else int(_res)
            print(f'MODE [{_res}] CHOSE FOR RESETING DATA BASE')
            _question = str(input('READY FOR RESET ? [default "N"] ')).lower()
            if _question == 'y':
                print("... RESETING DATA BASE PLEASE WAIT ...")
                _reset = _manager.reset(_res)
                print(f"RESET MODE [{_res}] DATA BASE [{_path}] IS [{'DONE' if _reset is True else 'CANT RESET'}]")
            else:
                print("RESET IS CANCELD")
        elif _inp in ('-1', 'cls', 'clear'):
            _CLEAR()
            print('PASSWORD MANAGER APP [VERSION 0.1]')
            print(f'\n\t< DATA BASE [{os.path.basename(_path)}] IS ACTIVE >')
            print("\t------------------------------------------------------")
            print('\n'.join(_menu))
        else:
            print('The Order Not Existed in Valid Order ! [Please Set Number For Command]')

    return 0

# KEY GENERATOR
def app_key_gen() -> int:
    _CLEAR()
    print("KEY GENERATOR [VERSION 0.1]")
    _menu = (
        '\n\n',
        '\t1  : GENERATE KEY',
        '\t2  : SET LENGTH [DEFAULT : 32]',
        '\t3  : SET CHARACTERS [DEFAULT : ASCII 32/126]',
        '\t4  : SET SKIP CHARACTERS ',
        '\t5  : SET COUNT MAKE [DEFAULT : 1]',
        '\t6  : SET PATH FOR SAVE RESULTS',
        '\t0  : EXIT',
        '\t-1 : Clear Display. U can Use "cls" or "clear"',
        '\n\n',
    )

    _length: int = 32
    _chars: str = None
    _skip: str = None
    _counter: int = 1
    _file: str = None

    _running = True
    print('\n'.join(_menu))
    while _running:
        _inp = str(input('-- /> '))
        _inp = int(_inp) if _inp.isdigit() else _inp.lower()
        if _inp == 0:
            _CLEAR()
            _running = False
            break
        elif _inp == 1:
            print("... GENERATE KEY ...")
            _maker = (my_passwords.key_maker(_length, _chars, _skip) for _ in range(0, _counter))
            _setup = f"COUNTER [{_counter}]\tLENGTH [{_length}]\tCHARS [{'ASCII 32/126' if _chars is None else _chars}]\tSKIP [{_skip}]\n\n"
            if _file:
                print("... RESULTS WRITE TO FILE ...")
                _file = os.path.realpath(_file)
                _info = "KEY GENERATOR [VERSION 0.1]"
                _wr = (_info, _setup)
                with open(_file, 'w') as f:
                    f.write('\t'.join(_wr))
                    for n, i in enumerate(_maker):
                        tmp = f"{n}\t{i}\n"
                        f.write(tmp)
                f.close()
                print(f"[{_counter}] GENERATED KEY SAVED INTO THE [{_file}]")
            else:
                print(f"... GENERATED KEY ...\n{_setup}")
                print(f"{'>'*_length}\n")
                print("\n".join(_maker))
                print('')
                print(f"{'<'*_length}\n")
        elif _inp == 2:
            print('... SET KEY LENGTH ...')
            _length = int(input('KEY LENGTH /> '))
            print(f'LENGTH [{_length}] IS SET')
        elif _inp == 3:
            print('... SET KEY CHARACTERS ...')
            _chars = str(input('KEY CHARACTERS /> '))
            print(f'CHARACTERS [{_chars}] IS SET')
        elif _inp == 4:
            print('... SET KEY SKIP CHARACTERS ...')
            _skip = str(input('KEY SKIP /> '))
            print(f'SKIP CHARACTERS [{_skip}] IS SET')
        elif _inp == 5:
            print('... SET COUNT KEY GENERATE ...')
            _counter = int(input('COUNT /> '))
            print(f'COUNT [{_counter}] IS SET')
        elif _inp == 6:
            print('... FILE FOR SAVE RESULT ...')
            _file = str(input('FILE PATH /> '))
            if _file not in ('', ' ', None):
                print(f'FILE [{os.path.realpath(_file)}] IS SET')
            else:
                print("FILE SET IS CANCELD")
        elif _inp in ('-1', 'cls', 'clear'):
            _CLEAR()
            print("KEY GENERATOR [VERSION 0.1]")
            print('\n'.join(_menu))
        else:
            print('The Order Not Existed in Valid Order ! [Please Set Number For Command]')

    return 0

# CIPHER
def app_cipher(_act_cipher: tuple = None) -> int:
    _CLEAR()
    print("CIPHER APP [VERSION 0.1]")
    _menu = (
        "\n\n",
        "\t1  : SETUP CIPHER.",
        "\t2  : INPUT TEXT ENCODE / DECODE.",
        "\t3  : FILE TEXT ENCODE / DECODE.",
        "\t4  : INPUT TEXT ONLY NESTED CIPHER ENCODE / DECODE.",
        "\t5  : FILE TEXT ONLY NESTED CIPHER ENCODE / DECODE.",
        "\t6  : SET FILE FOR SAVE RESULT.",
        "\t7  : UPDATE CIPHER.",
        "\t8  : GENERATE KEY.",
        "\t0  : Exit.",
        "\t-1 : CLear Display. U can Use 'cls' or 'clear'.",
        "\n\n",
    )
    if _act_cipher:
        assert len(_act_cipher) == 3
        _key, _method, _key_ci = _act_cipher
        _cls_cipher = my_passwords.Cipher(_key, _method, _key_ci)
        _cipher = True
    else:
        _key, _method, _key_ci = None, None, None
        _cls_cipher = None
        _cipher = False

    _path = None

    print('\n'.join(_menu))
    _running = True
    while _running:
        _inp = str(input('-- /> '))
        _inp = int(_inp) if _inp.isdigit() else _inp.lower()
        if _inp == 0:
            print("-- CLOSING --")
            _running = False
            _CLEAR()
        elif _inp == 1:
            print("SETUP CIPHER")
            if _cipher is True or _cls_cipher is not None:
                print("CIPHER IS SETUP ALLREADY")
                _question = str(input("ARE U WANT TO SETUP NEW CIPHER /> [default : 'N'] ")).lower()
                if _question == 'y':
                    print("SETUP NEW CIPHER")
                    _key = str(input("KEY /> [default : 'NONE'] "))
                    _key = None if _key in ('', ' ', None) else _key
                    _method = str(input("METHOD /> [default : 'NONE'] "))
                    _method = None if _method in ('', ' ', None) else _method
                    _key_ci = str(input("CIPHER KEY /> ['0' or '1']~[default : '0'] "))
                    _key_ci = False if _key_ci in ('0', '', ' ', None) else True

                    _cls_cipher = my_passwords.Cipher(_key, _method, _key_ci)
                    print("NEW CIPHER IS ACTIVE")
                else:
                    print("CANCELED BY USER")
            else:
                print("SETUP NEW CIPHER")
                _key = str(input("KEY /> [default : 'NONE'] "))
                _key = None if _key in ('', ' ', None) else _key
                _method = str(input("METHOD /> [default : 'NONE'] "))
                _method = None if _method in ('', ' ', None) else _method
                _key_ci = str(input("CIPHER KEY /> ['0' or '1']~[default : '0'] "))
                _key_ci = False if _key_ci in ('0', '', ' ', None) else True

                _cls_cipher = my_passwords.Cipher(_key, _method, _key_ci)
                print("NEW CIPHER IS ACTIVE")
        elif _inp == 2:
            print("INPUT TEXT CIPHER ENCODE / DECODE  [CRYPTING + CIPHER]")
            if _cls_cipher is None:
                print("CIPHER IS NOT SETUP PLEASE FIRST SETUPING CIPHER")
            else:
                print("SET MODE FOR ENCODE [1] OR DECODE [2]")
                _mode = str(input("MODE /> [default : '1'] "))
                _mode = 1 if _mode in ('1', '', ' ', None) else 2
                _txt = str(input("TEXT /> "))
                print("... WORKING ...")
                if _mode == 1:
                    _cip = _cls_cipher.encode(_txt)
                elif _mode == 2:
                    _cip = _cls_cipher.decode(_txt)
                if _path:
                    print("SAVE RESULT TO FILE")
                    _file = os.path.relpath(_path)
                    with open(_file, 'w') as f:
                        f.write(_cip)
                    f.close()
                    print("RESULT SAVED INTO THE FILE")
                else:
                    print("RESULT >>>>>>>>>>>>>>>>>>>")
                    print(f"{_cip}")
                    print("<<<<<<<<<<<<<<<<<<<<<<<END")
                del _txt, _cip
        elif _inp == 3:
            print("FILE TEXT CIPHER ENCODE / DECODE  [CRYPTING + CIPHER]")
            if _cls_cipher is None:
                print("CIPHER IS NOT SETUP PLEASE FIRST SETUPING CIPHER")
            else:
                print("SET MODE FOR ENCODE [1] OR DECODE [2]")
                _mode = str(input("MODE /> [default : '1'] "))
                _mode = 1 if _mode in ('1', '', ' ', None) else 2
                _inp_file = str(input("FILE PATH /> "))
                if _path is None:
                    _file = str(input("RESULT FILE PATH /> "))
                    _file = os.path.realpath(_file)
                else:
                    _file = os.path.realpath(_path)
                print("... WORKING ...")
                _inp_file = os.path.realpath(_inp_file)
                if os.path.exists(_inp_file):
                    with open(_inp_file, 'r') as f, open(_file, 'w') as of:
                        reader = f.read()

                        if _mode == 1:
                            _cip = _cls_cipher.encode(reader)
                        elif _mode == 2:
                            _cip = _cls_cipher.decode(reader)

                        of.write(_cip)
                    f.close()
                    of.close()
                    print(f"RESULT SAVED TO FILE [{_file}]")
                else:
                    print(f"FILE [{_inp_file}] NOT EXIST")
        elif _inp == 4:
            print("INPUT TEXT NESTED CIPHER ENCODE / DECODE")
            if _cls_cipher is None:
                print("CIPHER IS NOT SETUP PLEASE FIRST SETUPING CIPHER")
            else:
                print("SET MODE FOR ENCODE [1] OR DECODE [2]")
                _mode = str(input("MODE /> [default : '1'] "))
                _mode = 1 if _mode in ('1', '', ' ', None) else 2
                _method = str(input("NESTED CIPHER METHOD NAME /> [default : 'mb64'] "))
                _method = 'mb64' if _method in ('mb64', '', ' ', None) else _method
                _txt = str(input("TEXT /> "))
                print("... WORKING ...")
                if _mode == 1:
                    _nci = _cls_cipher.cipher_encode(_method, _txt)
                elif _mode == 2:
                    _nci = _cls_cipher.cipher_decode(_method, _txt)
                if _path:
                    print("SAVE RESULT TO FILE")
                    _file = os.path.relpath(_path)
                    with open(_file, 'w') as f:
                        f.write(_nci)
                    f.close()
                    print("RESULT SAVED INTO THE FILE")
                else:
                    print("RESULT >>>>>>>>>>>>>>>>>>>")
                    print(f"{_nci}")
                    print("<<<<<<<<<<<<<<<<<<<<<<<END")
                del _txt, _nci
        elif _inp == 5:
            print("FILE TEXT NESTED CIPHER ENCODE / DECODE")
            if _cls_cipher is None:
                print("CIPHER IS NOT SETUP PLEASE FIRST SETUPING CIPHER")
            else:
                print("SET MODE FOR ENCODE [1] OR DECODE [2]")
                _mode = str(input("MODE /> [default : '1'] "))
                _mode = 1 if _mode in ('1', '', ' ', None) else 2
                _method = str(input("NESTED CIPHER METHOD NAME /> [default : 'mb64'] "))
                _method = 'mb64' if _method in ('mb64', '', ' ', None) else _method
                _inp_file = str(input("FILE PATH /> "))
                if _path is None:
                    _file = str(input("RESULT FILE PATH /> "))
                    _file = os.path.realpath(_file)
                else:
                    _file = os.path.realpath(_path)
                print("... WORKING ...")
                _inp_file = os.path.realpath(_inp_file)
                if os.path.exists(_inp_file):
                    with open(_inp_file, 'r') as f, open(_file, 'w') as of:
                        reader = f.read()

                        if _mode == 1:
                            _nci = _cls_cipher.cipher_encode(_method, reader)
                        elif _mode == 2:
                            _nci = _cls_cipher.cipher_decode(_method, reader)

                        of.write(_nci)
                    f.close()
                    of.close()
                    print(f"RESULT SAVED TO FILE [{_file}]")
                else:
                    print(f"FILE [{_inp_file}] NOT EXIST")
        elif _inp == 6:
            print("SET FILE FOR SAVE RESULT")
            print("EVERY TIME SAVING RESULT DATA INTO THE FILE IS DELETED")
            _path = str(input("FILE PATH /> "))
            _path = None if _path in ('', ' ', None) else _path
            print(f"FILE [{os.path.realpath(_path)}] SET FOR WRITE RESULT")
        elif _inp == 7:
            print("UPDATE CIPHER")
            if _cls_cipher is None:
                print("CIPHER IS NOT SETUP PLEASE FIRST SETUPING CIPHER")
            else:
                print("UPDATE 'KEY'[1] OR 'METHOD'[2] OR 'BOTH'[3]")
                _upd_mode = str(input("SET UPDATE DATA /> [default : '3']")).lower()
                _upd_mode = '3' if _upd_mode in ('3', '', ' ', None) else _upd_mode
                if _upd_mode in ('1', 'key'):
                    print("UPDATE KEY")
                    _key = str(input("NEW KEY /> "))
                    _key = None if _key in ('', ' ', None) else _key
                    _key_ci = str(input("CIPHER KEY /> ['0' or '1'] [default : '0'] "))
                    _key_ci = False if _key_ci in ('0', '', ' ', None) else True
                    _cls_cipher.update_key(_key, _key_ci)
                    print("KEY IS UPDATED")
                elif _upd_mode in ('2', 'method'):
                    print("UPDATE CIPHER METHOD")
                    _all_method = _cls_cipher.all_method_supports()
                    print(f"ALL CIPHER METHOD SUPPORTS THIS CIPHER -> [{_all_method}]")
                    wrong_name = lambda x: (None, print(f"NO CIPHER METHOD NAMED [{x}] METHOD SET IS 'NONE'"))
                    check = lambda name: name if name in _all_method else wrong_name(name)[0]
                    _method = str(input("METHOD NAME /> [default : 'NONE'] "))
                    _method = None if _method in ('', ' ', None) else check(_method)
                elif _upd_mode in ('3', 'both'):
                    print("UPDATE BOTH 'KEY' AND 'METHOD'")
                    print("UPDATE KEY")
                    _key = str(input("NEW KEY /> "))
                    _key = None if _key in ('', ' ', None) else _key
                    _key_ci = str(input("CIPHER KEY /> ['0' or '1'] [default : '0'] "))
                    _key_ci = False if _key_ci in ('0', '', ' ', None) else True
                    _cls_cipher.update_key(_key, _key_ci)
                    print("KEY IS UPDATED")
                    print("UPDATE CIPHER METHOD")
                    _all_method = _cls_cipher.all_method_supports()
                    print(f"ALL CIPHER METHOD SUPPORTS THIS CIPHER -> [{_all_method}]")
                    wrong_name = lambda x: (None, print(f"NO CIPHER METHOD NAMED [{x}] METHOD SET IS 'NONE'"))
                    check = lambda name: name if name in _all_method else wrong_name(name)[0]
                    _method = str(input("METHOD NAME /> [default : 'NONE'] "))
                    _method = None if _method in ('', ' ', None) else check(_method)
                else:
                    print("CANCELED BY USER")
        elif _inp == 8:
            print("GENERATE KEY")
            _length = str(input("LENGTH KEY /> [default : 32] "))
            _length = int(_length) if _length.isdigit() else 32
            _gen_key = _cls_cipher.gen_key(_length)
            if _path is not None:
                print("WRITE TO RESULT FILE")
                _file = os.path.realpath(_path)
                with open(_file, 'w') as f:
                    f.write(_gen_key)
                f.close()
                print("GENERATED KEY SAVED TO FILE")
            else:
                print("GENERATED KEY >>>>>>>>>>>>")
                print(f"{_gen_key}")
                print("DONE <<<<<<<<<<<<<<<<<<<<<<")
        elif _inp in ('-1', 'cls', 'clear'):
            _CLEAR()
            print("CIPHER APP [VERSION 0.1]")
            print('\n'.join(_menu))
        else:
            print('The Order Not Existed in Valid Order ! [Please Set Number For Command]')

    return 0

# CRYPTO
def app_crypto() -> int:
    _CLEAR()
    print("CRYPTO APP [VERSION 0.1]")
    _menu = (
        "\n\n",
        "\t1  : INPUT TEXT ENCRYPTING OR DECRYPTING.",
        "\t2  : FILE TEXT ENCRYPTING OR DECRYPTING.",
        "\t3  : SET KEY.",
        "\t4  : SET PATH FOR SAVE RESULT.",
        "\t0  : EXIT.",
        "\t-1 : CLear Display. U can Use 'cls' or 'clear'.",
        "\n\n",
    )

    _key: str = None
    _path: str = None

    print('\n'.join(_menu))
    _running = True
    while _running:
        _inp = str(input('-- /> '))
        _inp = int(_inp) if _inp.isdigit() else _inp.lower()
        if _inp == 0:
            print("-- CLOSING --")
            _running = False
            _CLEAR()
        elif _inp == 1:
            print("INPUT ENCRYPTING OR DECRYPTING")
            _tmp_key = str(input("KEY /> ")) if _key is None else _key
            _txt = str(input('TEXT /> '))
            print("WORKING NOW ...")
            _crp = my_passwords.crypto(_txt, _tmp_key)
            if _path is not None:
                _file = os.path.realpath(_path)
                with open(_file, 'w') as f:
                    print("SAVEING TO FILE")
                    f.write(_crp)
                f.close()
                print(f"RESULT SAVED INTO THE FILE [{_file}]")
                del _crp, _tmp_key, _txt
            else:
                print("RESULTS >>>>")
                print(_crp)
                print("<<<< END")
                del _crp, _tmp_key, _txt
        elif _inp == 2:
            print("FILE ENCRYPTING OR DECRYPTING")
            print("SET CRYPTO KEY")
            _tmp_key = str(input("KEY /> ")) if _key is None else _key
            print("SET YOUR FILE FOR CRYPTING")
            _inp_file = os.path.realpath(str(input("FILE PATH /> ")))
            print("SET RESULT FILE")
            _file = os.path.realpath(str(input("RESULT PATH /> "))) if _path is None else os.path.realpath(_path)
            print(f"FILE [{_inp_file}] TO [{_file}]")
            _next = str(input("ARE U READY ? [default : 'Y'] ")).lower()
            if _next in ('y', '', ' ', None):
                print("... WORKING ...")
                with open(_inp_file, 'r') as f, open(_file, 'w') as of:
                    reader = f.read()
                    _crp = my_passwords.crypto(reader, _tmp_key)
                    of.write(_crp)
                f.close()
                of.close()
                print("... DONE ...")
                del _tmp_key, _inp_file, _file, reader, _crp
            else:
                print("CANCELD BY USER")
                del _tmp_key, _inp_file, _file
        elif _inp == 3:
            print("SET CRYPTO KEY")
            _key = str(input("KEY /> "))
            print(f"KEY [{_key}] IS SET")
        elif _inp == 4:
            print("SET FILE FOR SAVE RESULT")
            _path = str(input("PATH /> "))
            print("FOR RESULT FILE BE CLEANED EVERY TIME AND DELETED ALL DATA INTO THE FILE.")
            print(f"PATH [{os.path.realpath(_path)}] IS SET FOR SAVING RESULT")
        elif _inp in ('-1', 'cls', 'clear'):
            _CLEAR()
            print("CRYPTO APP [VERSION 0.1]")
            print('\n'.join(_menu))
        else:
            print('The Order Not Existed in Valid Order ! [Please Set Number For Command]')

    return 0

# UPDATE ACCOUNT
def app_update_account(_act_db: tuple = None) -> int:
    _CLEAR()
    print("UPDATE ACCOUNT DATA BASE APP [VERSION 0.1]")
    _menu = (
        "\n\n",
        "\t1  : UPDATE ACCOUNT.",
        "\t2  : RESET.",
        "\t0  : EXIT.",
        "\t-1 : CLear Display. U can Use 'cls' or 'clear'.",
        "\n\n",
    )

    if _act_db:
        assert len(_act_db) == 4
        _old_data = True
        _path, _method, _user, _pass = _act_db
    else:
        _old_data = False
        _path, _method, _user, _pass = None, None, None, None

    print('\n'.join(_menu))
    _running = True
    while _running:
        _inp = str(input('-- /> '))
        _inp = int(_inp) if _inp.isdigit() else _inp.lower()
        if _inp == 0:
            print("-- CLOSING --")
            _running = False
            _CLEAR()
        elif _inp == 1:
            print("UPDATE ACCOUNT")
            if _old_data:
                print("ACCOUNT DATA BASE IS SETTED IF YOU WANT TO OTHER DB PLEASE RESET '2'")
                print("SET NEW DATA")
                print("NEW 'USER NAME' & NEW 'PASSWORD' & NEW 'METHOD'.\n'USER NAME' & 'METHOD' IS OPTIONAL FOR CHANGE.")
                _new_user = str(input(f"NEW USER NAME /> [default '{_user}'] "))
                _new_user = _user if _new_user in ('', ' ', None) else _new_user
                _new_pass = str(input(f"NEW PASSWORD /> "))
                _new_method = str(input(f"NEW METHOD /> [default '{_method}'] "))
                _new_method = _method if _new_method in ('', ' ', None) else _new_method
                print("SET NEW DATA")
            else:
                print("SET DATA BASE PATH AND ACCOUNT DATA")
                _path = str(input('DATA BASE [PATH] /> '))
                _user = str(input('DATA BASE [USER NAME] /> '))
                _pass = str(input('DATA BASE [PASSWORD] /> '))
                _method = str(input('DATA BASE [CIPHER METHOD] /> '))
                print("SETTED DATA BASE FILE AND ACCOUNT DATA")
                print("SET NEW ACCOUNT DATA")
                print("ONLY 'PASSWORD' MUST BE CHANGED 'USER NAME' AND 'METHOD' IS OPTIONAL FO CHANGE")
                _new_user = str(input(f"NEW USER NAME /> [default '{_user}'] "))
                _new_user = _user if _new_user in ('', ' ', None) else _new_user
                _new_pass = str(input(f"NEW PASSWORD /> "))
                _new_method = str(input(f"NEW METHOD /> [default '{_method}'] "))
                _new_method = _method if _new_method in ('', ' ', None) else _new_method
                print("DATA BASE NEW ACCOUNT IS SETTED")

            _ready = str(input("ARE U READY /> [default : 'N'] ")).lower()
            if _ready == 'y':
                _path = os.path.relpath(_path)
                print('... WORKING ...')
                _upd = my_passwords.account_update(_path, _user, _pass, _new_user, _new_pass, _method, _new_method)
                print(f"UPDATE ACCOUNT IS [{'DONE' if _upd[0] is True else 'PROBLEM'}]\tOTHER : [{_upd[1]}]")
            else:
                print("CANCELED BY USER")
        elif _inp == 2:
            print('RESETING DATA')
            _old_data = False
            _path, _method, _user, _pass = None, None, None, None
            print('DATA IS RESET')
        elif _inp in ("-1", 'cls', 'clear'):
            _CLEAR()
            print("UPDATE ACCOUNT DATA BASE APP [VERSION 0.1]")
            print('\n'.join(_menu))
        else:
            print('The Order Not Existed in Valid Order ! [Please Set Number For Command]')

    return 0

# SETTING
def app_setting(_act_setting: tuple = None) -> int:
    _CLEAR()
    print("SETTING APP [VERSION 0.1]")
    _menu = (
        '\n\n',
        '\t1  : ADD OR UPDATE TO SETTING.',
        '\t2  : GET FROM SETTING.',
        '\t3  : CONNECT TO OTHER SETTING.',
        '\t4  : RESET SETTING. [CLEAR SETTING FILE]',
        '\t0  : EXIT.',
        "\t-1 : CLear Display. U can Use 'cls' or 'clear'.",
        '\n\n'
    )
    if _act_setting:
        assert len(_act_setting) == 3
        _path, _key, _method = _act_setting
    else:
        _path = str(input('SETTING PATH /> '))
        _key = str(input('SETTING KEY /> [default : No Secure] '))
        _key = None if _key in ('', ' ', None) else _key
        _method = str(input('SETTING METHOD /> [default : mb64] '))
        _method = 'mb64' if _method in ('', ' ', None) else _method

    _setting = Setting(_path, _key, _method)

    _CLEAR()
    print("SETTING APP [VERSION 0.1]")
    print('\n'.join(_menu))
    _running = True
    while _running:
        _inp = str(input('-- /> '))
        _inp = int(_inp) if _inp.isdigit() else _inp.lower()
        if _inp == 0:
            print("-- CLOSING --")
            _running = False
            _CLEAR()
        elif _inp == 1:
            print("ADD DATA TO SETTING")
            _name = str(input("NAME /> "))
            _path = str(input("DB FILE PATH /> "))
            _path = str(os.path.realpath(_path))
            _method = str(input("METHOD SECURE DB /> "))
            _method = 'rmb64' if _method in ('', ' ', None) else _method
            _user = str(input("DB USER NAME /> "))
            _pass = str(input("DB PASSWORD /> "))
            _data = (_path, _method, _user, _pass)
            _setting[_name] = format(_data)
            _setting.save_data()
            print(f"DATA [{_name}] ADDED TO SETTING")
        elif _inp == 2:
            print("GET DATA FROM SETTING")
            _name = str(input("NAME /> "))
            _data = _setting[_name]
            if _data is not None:
                if _data.startswith('(') and _data.endswith(')'):
                    _data = eval(_data)
                    print("-- DATA --")
                    print(f"PATH [{_data[0]}]\nMETHOD [{_data[1]}]\nUSER NAME [{_data[2]}]\nPASSWORD [{_data[3]}]")
                    print("-- - --")
                else:
                    print("[KEY] OR [METHOD] IS NOT VALID !")
            else:
                print(f"[{_name}] IS NOT EXISTED INTO THE SETTING")
        elif _inp == 3:
            print("CONNECT TO OTHER SETTING FILE")
            _really = str(input("ARE U REALLY TO CONNECT TO OTHER SETTING /> [default: 'N'] ")).lower()
            _really = 'n' if _really in ('', ' ', None) else _really
            if _really == 'y':
                _tmp = _path
                _path = str(input('SETTING PATH /> '))
                _key = str(input('SETTING KEY /> [default : No Secure] '))
                _key = None if _key in ('', ' ', None) else _key
                _method = str(input('SETTING METHOD /> [default : mb64] '))
                _method = 'mb64' if _method in ('', ' ', None) else _method
                print(f'... SETTING [{_tmp}] IS DISCONNECTED ...')
                _setting = Setting(_path, _key, _method)
                print(f'... SETTING [{_path}] IS CONNECTED ...')
            else:
                print('CANCELED BY USER')
        elif _inp == 4:
            print("RESETING SETTING FILE")
            _file = os.path.realpath(_path)
            if os.path.isfile(_file):
                print(f"< SETTING FILE [{_file}] READY FOR RESET >")
                print("ATTENTION :: RESET DATA IS DELETING ALL DATA INTO THE FILE !")
                _really = str(input("ARE U SURE /> [default : 'N'] ")).lower()
                _really = 'n' if _really in ('', ' ', None) else _really
                if _really == 'y':
                    print(f'... DISCONNECT THE SETTING FILE [{_file}] ...')
                    _setting = None
                    with open(_file, 'w') as f:
                        print("... DELETING DATA FROM SETTING ...")
                        f.write('{}')
                    f.close()
                    print(f"FILE [{_file}] IS RESET ALL DATA IS DELETED.")
                    input('PRESS [ENTER] FOR EXIT.')
                    _running = False
                    print('... CLOSING ...')
                    _CLEAR()
                    break
                else:
                    print('CANCELED BY USER')
        elif _inp in ('-1', 'cls', 'clear'):
            _CLEAR()
            print("SETTING APP [VERSION 0.1]")
            print('\n'.join(_menu))
        else:
            print('The Order Not Existed in Valid Order ! [Please Set Number For Command]')

    return 0

# MAIN
def main() -> int:
    _CLEAR()
    print("MY PASSWORD MANAGER APPLICATION [VERSION 0.1]")
    _menu = (
        "\n\n",
        "\t1  : PASSWORD MANAGER.",
        "\t2  : KEY GENERATOR.",
        "\t3  : TEXT CIPHER.",
        "\t4  : TEXT CRYPTO.",
        "\t5  : UPDATE ACCOUNT DATABASE.",
        "\t6  : CREATE OR UPDATE SETTING PASSWORD MANAGER.",
        "\t7  : ABOUT.",
        "\t0  : EXIT.",
        "\t-1 : CLear Display. U can Use 'cls' or 'clear'.",
        "\n\n",
    )
    print("\n\nSET YOUR SETTING PATH\n\tIF NOT SETTING FILE PRESS [ENTER] FOR SKIP\n\n")
    _setting_path = str(input('SETTING PATH /> '))
    _tmp_setting = os.path.realpath(_setting_path)
    _setting_path = _tmp_setting if os.path.isfile(_tmp_setting) else None
    if _setting_path not in ('', ' ', None):
        print('SECURE DATA IN SETTING IF NOT SECURED PRESS [ENTER] FOR SKIP [SETTING KEY]')
        _key = str(input('SETTING KEY /> '))
        _key = None if _key in ('', ' ', None) else _key
        _method = str(input('SETTING METHOD /> [default : mb64] '))
        _method = 'mb64' if _method in ('', ' ', None) else _method
        _settings = Setting(_setting_path, _key, _method)
    else:
        _settings = False

    def refresh() -> None:
        _CLEAR()
        print("MY PASSWORD MANAGER APPLICATION [VERSION 0.1]")
        print('\n'.join(_menu))

    refresh()
    _running = True
    while _running:
        _inp = str(input('-- /> '))
        _inp = int(_inp) if _inp.isdigit() else _inp.lower()
        if _inp == 0:
            print("-- CLOSING --")
            _running = False
            _CLEAR()
        elif _inp == 1:
            print("... PASSWORD MANAGER ...")
            _act_db = None
            if _settings:
                print("TYPE SETTING NAME IF DATABASE ADDED IN SETTING")
                _inp = str(input("SETTING NAME /> "))
                _act_db = _settings[_inp]
                _act_db = eval(_act_db)
                print(f"SETTING [{_inp}] [{'LOADED' if _act_db is not None else 'NOT EXISTS'}]")
            _app_man = app_password_manager(_act_db)
            print(f'PASSWORD MANAGER IS CLOSED / [{_app_man}]')
            refresh()
        elif _inp == 2:
            print("... KEY GENERATOR ...")
            _app_key = app_key_gen()
            print(f'KEY GENERATOR IS CLOSED / [{_app_key}]')
            refresh()
        elif _inp == 3:
            print("... TEXT CIPHER ...")
            _app_cipher = app_cipher()
            print(f'TEXT CIPHER IS CLOSED / [{_app_cipher}]')
            refresh()
        elif _inp == 4:
            print("... TEXT CRYPTO ...")
            _app_crypto = app_crypto()
            print(f'TEXT CRYPTO IS CLOSED / [{_app_crypto}]')
            refresh()
        elif _inp == 5:
            print("... ACCOUNT UPDATE  ...")
            _app_update_acc = app_update_account()
            print(f'ACCOUNT UPDATE IS CLOSED / [{_app_update_acc}]')
            refresh()
        elif _inp == 6:
            print("... SETTINGS PASSWORD MANAGER ...")
            _app_setting = app_setting()
            print(f'SETTING IS CLOSED / [{_app_setting}]')
            refresh()
        elif _inp in ('-1', 'cls', 'clear'):
            refresh()
        elif _inp == 7:
            _CLEAR()
            about = about_info()
            print(about)
            input("\tPRESS [ENTER]")
            refresh()
        else:
            print('The Order Not Existed in Valid Order ! [Please Set Number For Command]')

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
