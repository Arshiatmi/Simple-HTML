from core.error_handler import *
from core.color import *

def file_replace(file_name,text,replace):
    """
    Replace A Text To Another Text In A File
    """
    file = open(file_name)
    lines = file.readlines()
    file.close()
    lines = [i.replace(text,replace) for i in lines]
    file = open(file_name,"w")
    file.writelines(lines)
    file.close()

def text_replacer(text,search_array,replace_array):
    """
    Replace A List Of Strings To Another List Of Strings.
    """
    if type(text) == list:
        text = "".join(text)
    for i,j in zip(search_array,replace_array):
        text = text.replace(i,j)
    return text

def getProps(code):
    """
    This Function Will Get All Properties Of A Tag. For Example :
        @body( #myid , $myname , %myclass , bgcolor = "black" )
    Then This Function Will Return :
        {"_tagname":"body","_id":"myid","_name":"myname","_class":"myclass","bgcolor":"black"}
    """
    answer = {}
    if "(" in code and ")" in code:
        answer["_tagname"] = code.split("(")[0].replace("@","").strip()
        temp = code.split("(")[1].replace(")","").strip()
        for i in temp.split(","):
            if "=" in i:
                answer[i.split("=")[0].strip()] = i.split("=")[1].strip()
            elif ":" in i:
                answer[i.split(":")[0].strip()] = i.split(":")[1].strip()
            elif "=>" in i:
                answer[i.split("=>")[0].strip()] = i.split("=>")[1].strip()
            elif "->" in i:
                answer[i.split("->")[0].strip()] = i.split("->")[1].strip()
            elif i.startswith("#"):
                answer["_id"] = i[1:].strip()
            elif i.startswith("$"):
                answer["_name"] = i[1:].strip()
            elif i.startswith("%"):
                answer["_class"] = i[1:].strip()
        return answer
    else:
        answer["_tagname"] = code.replace("@","").strip()
        return answer

def smartIn(array,string):
    if string in array:
        return True
    for i in array:
        if string in i:
            return True
    return False

def getAllTags(line):
    """
    This Function Will Return All Tags In A Single Line. For Example :
        @title Test Title @@title
    Now Returns :
        ["@title","@@title"]
    """
    line = line.strip()
    ends = [i for i in line.split(" ") if i.startswith("@@")]
    lines = " ".join([i for i in line.split(" ") if not i.startswith("@@")])
    starts = []
    temp = ""
    lines = lines.split(" ")
    c = 0
    while c < len(lines):
        if lines[c].startswith("@"):
            temp += lines[c]
            c2 = 0
            if smartIn(lines,")") and smartIn(lines,"("):
                while ")" not in lines[c + c2]:
                    c2 += 1
                    temp += lines[c + c2]
                starts.append(temp.strip())
                temp = ""
            else:
                starts.append(lines[c])
        c += 1
    return {"start":starts,"end":ends}

def createHTMLTag(details):
    """
    This Function Will Create HTML Tags Using The Details That Created In
    getProps Function. For Example :
        {"_tagname":"body","_id":"myid","_name":"myname","_class":"myclass","bgcolor":"black"}
    Will Returns :
        <body id="myid" name="myname" class="myclass" bgcolor="black">
    """
    tagname = details["_tagname"]
    id = details.get("_id","")
    name = details.get("_name","")
    tagClass = details.get("_class","")
    answer = "<" + tagname
    del details["_tagname"]
    if id:
        answer += f" id=\"{id}\""
        del details["_id"]
    if name:
        answer += f" name=\"{name}\""
        del details["_name"]
    if tagClass:
        answer += f" class=\"{tagClass}\""
        del details["_class"]
    for i,j in details.items():
        answer += f" {i}={j}"
    answer += ">"
    return answer

def removeSpace(string):
    tempString = ""
    for i in string.strip().split(" "):
        tempString += i
    return tempString

def euqals(string1,string2):
    if removeSpace(string1) == removeSpace(string2):
        return True
    return False

def intelligence_replace(text,searchString,replaceString):
    if removeSpace(searchString) in removeSpace(text):
        pass
