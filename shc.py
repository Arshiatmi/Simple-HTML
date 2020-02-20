import sys
from core.color import setColor
from core.functions import *
from core.error_handler import *

helperVariable = False
try:
    file_name = sys.argv[1]
except:
    print(setColor(f"""Usage : {sys.argv[0]} [Your Code Name].sht""","green"))

try:
    handler = open(file_name)
    l = handler.readlines()
    handler.close()
except:
    createError(setColor("FileNotFound","red"),"The Target File Not Found !",[],0)
