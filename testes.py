import os
import glob
import time
import pyaes
from pathlib import Path
dire=[]
c = r"C:\Users\Emanuel Energia\Downloads\taskbarx-1-7-6-0\zh-TW"
pasta = Path.home() / "Downloads"
for diretorio, subpastas, arquivos in os.walk(pasta):
    if (diretorio[0]!='.'):
        for arquivo in arquivos:
            dire.append(os.pardir.join(diretorio).replace(".", ""))
for l in dire:
    print(l)