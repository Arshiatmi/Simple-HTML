import sys
from core.color import *

def indexExists(array,index):
    try:
        array[index]
        return True
    except:
        return False

def createWarning(title,text,code = [],warn_line = 0):
    """
    This Function Will Create Warning With ([title] -> Warning Title) And ([text] -> Warning Text)
    And ([code] -> The Code As An Array) And ([warn_line] -> The Line That Warning Exists).
    """
    title = setColor(title,"yellow")
    code_part = []
    if not code and not warn_line:
        print(title + " : " + text)
        return
    if warn_line == 0:
        print(setColor("\nWarning :\n","yellow"))
        code_part.append(code[warn_line].strip())
        print(f"""\t{setColor(f"-> {warn_line + 1} : {code_part[0]}","yellow")}""")
        try:
            code_part.append(code[warn_line + 1].strip())
            print(f"\t{warn_line + 2} : {code_part[1]}")
        except:
            pass
        try:
            code_part.append(code[warn_line + 2].strip())
            print(f"\t{warn_line + 3} : {code_part[2]}")
        except:
            pass
        print(f"""

{title} : {text}
""")
    elif warn_line >= len(code) - 1:
        print(setColor("\nWarning :\n","yellow"))
        try:
            code_part.append(code[warn_line - 2].strip())
            print(f"\t{warn_line - 1} : {code_part[0]}")
        except:
            pass
        try:
            code_part.append(code[warn_line - 1].strip())
            print(f"\t{warn_line} : {code_part[1]}")
        except:
            pass
        code_part.append(code[warn_line].strip())
        print(f"""\t{setColor(f"-> {warn_line + 1} : {code_part[2]}","yellow")}""")
        print(f"""

{title} : {text}
""")
    else:
        print(setColor("\nWarning :\n","yellow"))
        try:
            code_part.append(code[warn_line - 1].strip())
            print(f"\t{warn_line} : {code_part[0]}")
        except:
            pass
        code_part.append(code[warn_line].strip())
        print(f"""\t{setColor(f"-> {warn_line + 1} : {code_part[1]}","yellow")}""")
        try:
            code_part.append(code[warn_line + 1].strip())
            print(f"\t{warn_line + 2} : {code_part[2]}")
        except:
            pass
        print(f"""

{title} : {text}
""")

def createError(title,text = "An Error Detected !",code = [],error_line = 0):
    """
    This Function Will Create Error With ([title] -> Error Title) And ([text] -> Error Text)
    And ([code] -> The Code As An Array) And ([error_line] -> The Line That Error Exists).
    """
    title = setColor(title,"red")
    if not code and not error_line:
        print(title + " : " + text)
        sys.exit()
    code_part = []
    if error_line == 0:
        print(setColor("\Error :\n","red"))
        code_part.append(code[error_line].strip())
        print(f"""\t{setColor(f"-> {error_line + 1} : {code_part[0]}","red")}""")
        try:
            code_part.append(code[error_line + 1].strip())
            print(f"\t{error_line + 2} : {code_part[1]}")
        except:
            pass
        try:
            code_part.append(code[error_line + 2].strip())
            print(f"\t{error_line + 3} : {code_part[2]}")
        except:
            pass
        print(f"""

{title} : {text}
""")
        sys.exit()
    elif error_line >= len(code) - 1:
        print(setColor("\Error :\n","red"))
        try:
            code_part.append(code[error_line - 2].strip())
            print(f"\t{error_line - 1} : {code_part[0]}")
        except:
            pass
        try:
            code_part.append(code[error_line - 1].strip())
            print(f"\t{error_line} : {code_part[1]}")
        except:
            pass
        code_part.append(code[error_line].strip())
        print(f"""\t{setColor(f"-> {error_line + 1} : {code_part[2]}","red")}""")
        print(f"""

{title} : {text}
""")
        sys.exit()
    else:
        print(setColor("\Error :\n","red"))
        try:
            code_part.append(code[error_line - 1].strip())
            print(f"\t{error_line} : {code_part[0]}")
        except:
            pass
        code_part.append(code[error_line].strip())
        print(f"""\t{setColor(f"-> {error_line + 1} : {code_part[1]}","red")}""")
        try:
            code_part.append(code[error_line + 1].strip())
            print(f"\t{error_line + 2} : {code_part[2]}")
        except:
            pass
        print(f"""

{title} : {text}
""")
        sys.exit()
