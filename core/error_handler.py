import sys
from core.color import *

def createError(title,text = setColor("An Error Detected !","red"),code = [],error_line = 0):
    """
    This Function Will Create Error With ([title] -> Error Title) And ([text] -> Error Text)
    And ([code] -> The Code In Array) And ([error_line] -> The Line That Error Exists).
    """
    if not code and not error_line:
        print(title + " : " + text)
        sys.exit()
    code_part = []
    if code_part == 0:
        code_part.append(code[error_line])
        code_part.append(code[error_line + 1])
        code_part.append(code[error_line + 2])
        print(f"""Error :

{setColor(f"-> {error_line} : {code_part[0]}","red")}
{error_line + 1} : {code_part[1]}
{error_line + 2} : {code_part[2]}

{title} : {text}
""")
        sys.exit()
    elif code_part == len(code) - 1:
        code_part.append(code[error_line - 2])
        code_part.append(code[error_line - 1])
        code_part.append(code[error_line])
        print(f"""Error :

{error_line - 2} : {code_part[0]}
{error_line - 1} : {code_part[1]}
{setColor(f"-> {error_line} : {code_part[2]}","red")}

{title} : {text}
""")
        sys.exit()
    else:
        code_part.append(code[error_line - 1])
        code_part.append(code[error_line])
        code_part.append(code[error_line + 1])
        print(f"""Error :

{error_line - 1} : {code_part[0]}
{setColor(f"-> {error_line} : {code_part[1]}","red")}
{error_line + 1} : {code_part[2]}

{title} : {text}
""")
        sys.exit()
