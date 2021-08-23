###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT
import sys
import argparse

from typing import Union

# IMPORT MY PASSWORD
import my_passwords


# PASSWORD
def password_man(cmd: dict) -> Union[bool, int, str]:
    if cmd['Command'] == 'accup':
        return my_passwords.account_update(cmd['database'], cmd['Username'], cmd['Password'], cmd['new_username'], cmd['new_password'], cmd['cipher_method'], cmd['new_cipher_method'])

    if cr := cmd.get('custom_return'):
        cmd['return'] = cr

    mng = my_passwords.Manager
    mng.METHOD = cmd['cipher_method']
    mng = mng(cmd['database'], cmd['Username'], cmd['Password'])

    com = cmd['Command']
    if com == 'add':
        return mng.add_pass(cmd['name'], cmd['password'], cmd['url'], cmd['more'])

    elif com == 'get':
        return mng.get_pass(cmd['name'], cmd['return'])

    elif com == 'up':
        return mng.update_pass(cmd['name'], cmd['password'], cmd['url'], cmd['more'])

    elif com == 'del':
        return mng.del_pass(cmd['name'], secure=True)

    elif com == 'exists':
        return mng.exists(cmd['name'])

    elif com == 'count':
        return mng.counter_password()

    elif com == 'reset':
        return mng.reset(1)

    elif com == 'removeall':
        return mng.reset(2)

# MAIN FUNCTION
def main(argv: list[str]) -> int:
    command = ('add', 'get', 'up', 'del', 'reset', 'count', 'exists', 'removeall', 'accup')
    ret_c = ('all', 'id', 'name', 'password', 'url', 'more', 'settime', 'lastupdate')
    ci_m = ('b64','ab64','mb64','eb64','lb64','rb64','rab64','rmb64','reb64','rlb64')
    dfa = {'cipher': 'rmb64', 'database': './data/db.mps', 'ret': 'password'}
    argument_parse = argparse.ArgumentParser(prog="MyPasswords", description="Simple Password Manager")

    # Add Arguments
    argument_parse.add_argument('Username', type= str, help= 'Your User Name')
    argument_parse.add_argument('Password', type= str, help= 'Your Password')
    argument_parse.add_argument('Command', choices=command, help= 'What to do !?')
    argument_parse.add_argument('--new_username', '-nu', type= str, help= 'New User Name')
    argument_parse.add_argument('--new_password', '-np', type= str, help= 'New Password')
    argument_parse.add_argument('--new_cipher_method', '-ncm', choices= ci_m, type= str, help= 'New Method')
    argument_parse.add_argument('--name', '-n', type= str, help= 'Password Name')
    argument_parse.add_argument('--password', '-p', type= str, help= 'Password')
    argument_parse.add_argument('--url', '-u', type= str, help= 'Set URL for this Password')
    argument_parse.add_argument('--more', '-m', type= str, help= 'Set More Info for This Password')
    argument_parse.add_argument('--return', '-r', choices=ret_c, default=dfa['ret'] ,type= str, help= 'Return Get')
    argument_parse.add_argument('--custom_return', '-cr',type= str, help= 'Return Get')
    argument_parse.add_argument('--database', '-db', default=dfa['database'],type= str, help= 'Data Base Path')
    argument_parse.add_argument('--cipher_method', '-cm', choices= ci_m, default= dfa['cipher'], type= str, help= 'Chose Cipher Method')

    arguments = {k:v for k, v in argument_parse.parse_args()._get_kwargs()}

    results = password_man(arguments)
    print(results)
    return 0

if __name__ == "__main__":
    exit(main(sys.argv))
