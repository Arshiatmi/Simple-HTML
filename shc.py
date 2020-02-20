import sys
from color import setColor

try:
    file = sys.argv[1]
    print(file)
except:
    print(setColor(f"""Usage : {sys.argv[0]} [Your Code Name].sht""","green"))
