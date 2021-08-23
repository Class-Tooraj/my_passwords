###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################
from manager import crypto, key_maker, Cipher, Manager, account_update

# TEST CRYPTO
def test_crypting(inp: str, key: str) -> bool:
    cr = crypto(inp, key)
    de = crypto(cr, key)
    try:
        assert cr != inp and de == inp
        return True
    except AssertionError:
        print(f"{AssertionError}")
        return False

# TEST KEY MAKER
def test_key_maker(l: int = None, c: str = None, s: str = None) -> bool:
    mk = key_maker(length = l, chars = c, skip = s)
    c = tuple(chr(i) for i in range(32, 127)) if c is None else c

    c_char = all([(it in c) for it in mk])
    c_skip = all([(it not in mk) for it in s])

    try:
        assert len(mk) == l and c_char is True and c_skip is True
        return True
    except AssertionError:
        print(f"{AssertionError}")
        return False

# TEST CIPHER
def test_cipher(txt: str, k:str = None, m:str = None, ck:bool = None) -> bool:
    cip = Cipher(k, m, ck)
    en_c = cip.encode(txt)
    de_c = cip.decode(en_c)
    c_en = cip.cipher_encode('ab64', txt)
    c_de = cip.cipher_decode('ab64', c_en)
    try:
        assert cip != txt and de_c == txt and c_en != txt and c_de == txt
        return True
    except AssertionError:
        print(f"{AssertionError}")
        return False

# TEST MANAGER
def test_manager(user:str, password: str) -> bool:
    data = ['Test', 'TEST123456', 'www.test.test', 'Test is TeSt More Is tEsT']
    up = ['Test', 'UPD123', 'www.update.up', 'UPdate']
    mng = Manager(":memory:", user, password)
    nw = mng.add_pass(*data)
    gt = mng.get_pass(data[0], 'name,password,url,more').split(',')
    upd = mng.update_pass(*up)
    gtu = mng.get_pass(data[0], 'name,password,url,more').split(',')
    rs = mng.reset(2)
    try:
        assert nw is True and gt == data and upd is True and gtu == up and rs is True
        return True
    except AssertionError:
        print(f"{AssertionError}")
        return False

# TEST ACCOUNT UPDATE
def test_account_update(user: str, password: str, new_user: str, new_password: str, old_method: str = None, new_method: str = None, db_size: int = 30, path: str = None) -> bool:
    path = './test/t.db' if path is None else path
    def make() -> bool:
        m_val = ((f'Name_{i}', f'Password_{i}', f'URL_{i}', f'More_{i}') for i in range(0, db_size))
        db = Manager(path, user, password)
        gen = (db.add_pass(*i) for i in m_val)
        tmp = []
        for i in gen:
            tmp.append(i)
        return all(tmp)
    mk_db = make()
    if mk_db is True:
        return account_update(path, user, password, new_user, new_password, old_method, new_method)[0]
    else:
        return False

if __name__ == "__main__":
    print(f"{'':>5}-> START TESTS <-", end='\n\n')

    t_cp = test_crypting('73$7+$TR!N6', '•ÄæTESTµÆü')
    print(f"{'':>5}Crypting  :: {t_cp}", end='\n\n')
    t_km = test_key_maker(64, s= '*\\.')
    print(f"{'':>5}KeyMaker :: {t_km}", end='\n\n')
    t_ci = test_cipher('321-- T3$T $TR!N6 --123')
    print(f"{'':>5}Cipher :: {t_ci}", end='\n\n')
    t_ma = test_manager('test', '*TEST*')
    print(f"{'':>5}Manager :: {t_ma}", end='\n\n')
    t_au = test_account_update('test', '*TEST*', 'NEW_USER', '**NEW_PASSWORD**', 'rmb64', 'mb64', 16, None)
    print(f"{'':>5}AccountUpdate :: {t_au}", end='\n\n')

    print(f"{'':>5}->    DONE    <-", end='\n')
