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
        1.   python(3) {sys.argv[0]} [Your Code Name].sw
        2.   python(3) {sys.argv[0]} [Your Project Folder Name]""","green"))
    sys.exit()

if ".sw" in sys.argv[1]:
    try:
        handler = open(file_name)
        l = handler.readlines()
        handler.close()
    except FileNotFoundError or FileExistsError:
        createError("FileNotFound","The Target File Not Found !")
        sys.exit()
    except IOError:
        createError("IOError","Unable To Read The File !")
        sys.exit()
    except:
        createError("UnexpectedError","An Unexpected Error Raised During Reading The File :(")
        sys.exit()
    handler = open(file_name.replace(".sw","") + ".html","w")
    handler.writelines(translate(l))
    handler.close()
    print(setColor(f"Compiled Successfully ! HTML Output Is ","green") + setColor(f"""{file_name.replace(".sw","") + ".html"}""","lightyellow") + setColor(" .","green"))
elif "." not in sys.argv[1]:
    if not os.path.exists(sys.argv[1] + ".output"):
        os.system(f"""mkdir {sys.argv[1] + ".output"}""")
    targetFiles = [i for i in os.listdir(sys.argv[1]) if i[i.rfind("."):] == ".sw"]
    for i in targetFiles:
        if "/" in sys.argv[1]:
            inFile = open(sys.argv[1] + "/" + i)
            l = inFile.readlines()
            inFile.close()
            outFile = open(sys.argv[1] + ".output" + "/" + i.replace(".sw","") + ".html","w")
            outFile.writelines(translate(l))
            outFile.close()
        elif "\\" in sys.argv[1]:
            inFile = open(sys.argv[1] + "\\" + i)
            l = inFile.readlines()
            inFile.close()
            outFile = open(sys.argv[1] + ".output" + "\\" + i.replace(".sw","") + ".html","w")
            outFile.writelines(translate(l))
            outFile.close()
        else:
            inFile = open(sys.argv[1] + "/" + i)
            l = inFile.readlines()
            inFile.close()
            outFile = open(sys.argv[1] + ".output" + "/" + i.replace(".sw","") + ".html","w")
            outFile.writelines(translate(l))
            outFile.close()
    print(setColor(f"Compiled Successfully ! HTML Output Is In ","green") + setColor(f"""{sys.argv[1] + ".output"}""","lightyellow") + setColor(" .","green"))
else:
    form = sys.argv[1]
    form = form[form.rfind("."):]
    try:
        codeFile = open(sys.argv[1])
        lines = codeFile.readlines()
        codeFile.close()
    except FileNotFoundError or FileExistsError:
        createError("FileNotFound","The Target File Not Found !")
        sys.exit()
    except IOError:
        createError("IOError","Unable To Read The File !")
        sys.exit()
    except:
        createError("UnexpectedError","An Unexpected Error Raised During Reading The File :(")
        sys.exit()
    createWarning("Format Warning",f"Seems The File Format {form} Is Not .sw ! Thats Better To Be [.sw] .")
    if not isSW("".join(lines)):
        createError("CompileError","An Error In Compiling The Code ! Seems Its Not A Simple Web Code .")
        sys.exit()
    outName = sys.argv[1].replace(sys.argv[1][sys.argv[1].rfind("."):],"") + ".html"
    handler = open(outName,"w")
    handler.writelines(translate(lines))
    handler.close()
    print(setColor(f"Format Doesn't Correct But Anyway Compiled Successfully ! HTML Output Is ","green") + setColor(f"""{outName}""","lightyellow") + setColor(" .","green"))
    sys.exit()
