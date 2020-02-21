#!/usr/share/python3

import sys
from core.color import setColor
from core.functions import *
from core.error_handler import *
from core.compiler import *

helperVariable = False
try:
    file_name = sys.argv[1]
except:
    print(setColor(f"""Usage : python(3) {sys.argv[0]} [Your Code Name].sht""","green"))
    sys.exit()

try:
    handler = open(file_name)
    l = handler.readlines()
    handler.close()
except:
    createError(setColor("FileNotFound","red"),"The Target File Not Found !",[],0)

f = open(file_name.replace(".sht","") + ".html","w")
f.writelines(translate(l))
f.close()
