import sys
from core.color import *

def indexExists(array,index):
    try:
        array[index]
        return True
    except:
        return False


def createError(title,text = setColor("An Error Detected !","red"),code = [],error_line = 0):
    """
    This Function Will Create Error With ([title] -> Error Title) And ([text] -> Error Text)
    And ([code] -> The Code In Array) And ([error_line] -> The Line That Error Exists).
    """
    if not code and not error_line:
        print(title + " : " + text)
        sys.exit()
    code_part = []
    if error_line == 0:
        print("Error :")
        code_part.append(code[error_line])
        print(f"""{setColor(f"-> {error_line} : {code_part[0]}","red")}""")
        try:
            code_part.append(code[error_line + 1])
            print(f"{error_line + 1} : {code_part[1]}")
        except:
            pass
        try:
            code_part.append(code[error_line + 2])
            print(f"{error_line + 2} : {code_part[2]}")
        except:
            pass
        print(f"""

{title} : {text}
""")
        sys.exit()
    elif error_line >= len(code) - 1:
        print("Error :")
        try:
            code_part.append(code[error_line - 2])
            print(f"{error_line - 2} : {code_part[0]}")
        except:
            pass
        try:
            code_part.append(code[error_line - 1])
            print(f"{error_line - 1} : {code_part[1]}")
        except:
            pass
        code_part.append(code[error_line])
        print(f"""{setColor(f"-> {error_line} : {code_part[2]}","red")}""")
        print(f"""

{title} : {text}
""")
        sys.exit()
    else:
        print("Error :")
        try:
            code_part.append(code[error_line - 1])
            print(f"{error_line - 1} : {code_part[0]}")
        except:
            pass
        code_part.append(code[error_line])
        print(f"""{setColor(f"-> {error_line} : {code_part[1]}","red")}""")
        try:
            code_part.append(code[error_line - 1])
            print(f"{error_line + 1} : {code_part[2]}")
        except:
            pass
        print(f"""

{title} : {text}
""")
        sys.exit()
