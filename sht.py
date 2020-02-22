#!/usr/share/python3

import sys, os
from core.color import setColor
from core.functions import *
from core.error_handler import *
from core.compiler import *

helperVariable = False
try:
    file_name = sys.argv[1]
except:
    print(setColor(f"""Usages :
        1.   python(3) {sys.argv[0]} [Your Code Name].sht
        2.   python(3) {sys.argv[0]} [Your Project Folder Name]""","green"))
    sys.exit()

if ".sht" in sys.argv[1]:
    try:
        handler = open(file_name)
        l = handler.readlines()
        handler.close()
    except:
        createError("FileNotFound","The Target File Not Found !")
        sys.exit()
    handler = open(file_name.replace(".sht","") + ".html","w")
    handler.writelines(translate(l))
    handler.close()
    print(setColor(f"Compiled Successfully ! HTML Output Is ","green") + setColor(f"""{file_name.replace(".sht","") + ".html"}""","lightyellow") + setColor(" .","green"))
elif "." not in sys.argv[1]:
    if not os.path.exists(sys.argv[1] + ".output"):
        os.system(f"""mkdir {sys.argv[1] + ".output"}""")
    targetFiles = [i for i in os.listdir(sys.argv[1]) if i[i.rfind("."):] == ".sht"]
    for i in targetFiles:
        if "/" in sys.argv[1]:
            inFile = open(sys.argv[1] + "/" + i)
            l = inFile.readlines()
            inFile.close()
            outFile = open(sys.argv[1] + ".output" + "/" + i.replace(".sht","") + ".html","w")
            outFile.writelines(translate(l))
            outFile.close()
        elif "\\" in sys.argv[1]:
            inFile = open(sys.argv[1] + "\\" + i)
            l = inFile.readlines()
            inFile.close()
            outFile = open(sys.argv[1] + ".output" + "\\" + i.replace(".sht","") + ".html","w")
            outFile.writelines(translate(l))
            outFile.close()
        else:
            inFile = open(sys.argv[1] + "/" + i)
            l = inFile.readlines()
            inFile.close()
            outFile = open(sys.argv[1] + ".output" + "/" + i.replace(".sht","") + ".html","w")
            outFile.writelines(translate(l))
            outFile.close()
    print(setColor(f"Compiled Successfully ! HTML Output Is In ","green") + setColor(f"""{sys.argv[1] + ".output"}""","lightyellow") + setColor(" .","green"))
else:
    form = sys.argv[1]
    form = form[form.rfind("."):]
    createError("Format Error",f"Sorry The Format {form} Not Supported ! Format Should Be [.sht] .")
    sys.exit()
