from pathlib import Path
#base_path = r'c:\dir\with\bunch\of\files'
base_path=Path.home() / "Downloads"
filename_filter = ["*.txt","*.xls","*.kk"]
pastas=[]
def k():
    for t in filename_filter:
        for filename in Path(base_path).rglob(t):
            print(filename)
            pastas.append(filename)
k()
#print(pastas[0])
def form(var):
    #print(f"Variavel: {var}")
    var=var.__str__()
    l=[]
    c=int(len(var)-1)
    o=r"\ ".replace(" ","")
    while c >=0:
        if var[c]==o:
            #print('final')
            break
        else:
            l.append(var[c])
        c=c-1
    v=int(len(l)-1)
    msg=''
    while v >=0:
        msg=msg+l[v]
        v=v-1
    #print(msg)
    return msg
for h in pastas:
    print(form(h))
#print(form(pastas[0]))
