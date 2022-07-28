from pathlib import Path
base_path=Path.home() / "Downloads"
filename_filter = ["*.txt","*.xls","*.kk"]
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
cu=varer()
print(cu)