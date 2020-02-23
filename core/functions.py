from core.error_handler import *
from core.color import *
from core.lists import *
import re

def file_replace(file_name,text,replace):
    """
    Input :
        file_name   ->  String  { The File Name }
        text        ->  String  { Text That Code Will Find This Strings }
        replace     ->  String  { Text That Will Be Replaced . }
    Output:
        null
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
    Input :
        text           ->  String  { The Full Text }
        search_array   ->  List    { List Of Strings That Wanted To Be Replaced . }
        replace_array  ->  List    { List Of Strings That Will Be Replaced . }
    Output:
        text           ->  String  { The Replaced Answer }
    Replace A List Of Strings To Another List Of Strings.
    """
    if type(text) == list:
        text = "".join(text)
    for i,j in zip(search_array,replace_array):
        text = text.replace(i,j)
    return text

def correctIn(s1,s2,tars = ["=>","->","=",":"]):
    """
    Input :
        s1    ->  String  { First String }
        s2    ->  String  { Second String }
        tars  ->  List    { List Of Signs }
    Output:
        True / False  ->  Bool  { Is This Ok Or Not ? }  # See In Example Down There

    Checks If A String Exists In Another String In Some Specific Situations.
    For Example :
        s1  ---   style=>"color:red"
        s2  ---   :
    Returns False. Because : It Isnt First Element Of Tars That Exists Is String.
     But Another Example :
        s1  ---   style=>"color:red"
        s2  ---   =>
    Return True Because Its First Of Tars That Exists In String.
    """
    tar = s1.split(s2)
    if len(tar) == 1:
        return False
    l = tar[0]
    for i in tars:
        if i in l:
            return False
    return True

def getProps(code,fc="",line_number=0):
    """
    Input :
        code        ->  String  { A Line Of Code To Get Properties }
        fc          ->  String  { Full Code }
        line_number ->  Int     { Current Line ( Line Of code Variable ) }
    Output:
        answer      ->  Dict  { Translated Code }
    This Function Will Get All Properties Of A Tag. For Example :
        @body( #myid , $myname , %myclass , bgcolor = "black" )
    Then This Function Will Return :
        {"_tagname":"body","_id":"myid","_name":"myname","_class":"myclass","bgcolor":"black"}
    """
    answer = {}
    if "(" in code:
        if code.find(")") == -1:
            createError(setColor("Syntax Error","red"),"An Error In Parsing. Did You Forget ')' At The End ??? ",fc,line_number)
        answer["_tagname"] = code.split("(")[0].replace("@","").strip()
        temp = code.split("(")[1].replace(")","").strip()
        for i in temp.split(","):
            if correctIn(i,"=>"):
                answer[i.split("=>")[0].strip()] = i.split("=>")[1].strip()
            elif correctIn(i,"->"):
                answer[i.split("->")[0].strip()] = i.split("->")[1].strip()
            elif correctIn(i,"="):
                answer[i.split("=")[0].strip()] = i.split("=")[1].strip()
            elif ":" in i:
                answer[i.split(":")[0].strip()] = ":".join(i.split(":")[1:]).strip()
            if i.startswith("#"):
                answer["_id"] = i[1:].strip()
            if i.startswith("$"):
                answer["_name"] = i[1:].strip()
            if i.startswith("%"):
                answer["_class"] = i[1:].strip()
        return answer
    elif "|" in code:
        if code.count("|") < 2:
            createError(setColor("Syntax Error","red"),"An Error In Parsing. Did You Forget A '|' ??? ",fc,line_number)
        answer["_tagname"] = code.split("|")[0].replace("@","").strip()
        temp = code.split("|")[1].replace("|","").strip()
        for i in temp.split(","):
            if correctIn(i,"=>"):
                answer[i.split("=>")[0].strip()] = i.split("=>")[1].strip()
            elif correctIn(i,"->"):
                answer[i.split("->")[0].strip()] = i.split("->")[1].strip()
            elif correctIn(i,"="):
                answer[i.split("=")[0].strip()] = i.split("=")[1].strip()
            elif ":" in i:
                answer[i.split(":")[0].strip()] = ":".join(i.split(":")[1:]).strip()
            if i.startswith("#"):
                answer["_id"] = i[1:].strip()
            if i.startswith("$"):
                answer["_name"] = i[1:].strip()
            if i.startswith("%"):
                answer["_class"] = i[1:].strip()
        return answer
    else:
        answer["_tagname"] = code.replace("@","").strip()
        return answer

def smartIn(array,string):
    """
    Input :
        array        ->  List  { A list }
        string       ->  String  { A String }
    Output:
        True / False      ->  Bool  { Checks If String Is In List Or A Part Of Strings Of List Or Not . }
    Checks If A String Exists In An Array Or Not.
    """
    if string in array:
        return True
    for i in array:
        if string in i:
            return True
    return False

def isHTML(tagName):
    """
    Input :
        tagName       ->  String  { Tag Name }
    Output:
        True / False  ->  Bool  { Checks If Its An HTML Tag Or Not }
    """
    file = open("repos/html.txt")
    tags = [i.strip() for i in file.readlines()]
    file.close()
    if tagName.strip() in tags:
        return True
    return False

def getAllTags(line):
    """
    Input :
        line                     ->  String  { The Line }
    Output:
        {"start":[],"end":[]}  ->  Dict  { All Tags Exists In Line }
    This Function Will Return All Tags In A Single Line. For Example :
        @title Test Title @@title
    Now Returns :
        {"start":["@title"],"end":["@@title"]}
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
            if not isHTML(lines[c].replace("@","").replace("("," ").replace("|"," ").split(" ")[0]):
                c += 1
                continue
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
    Input :
        details     ->  Dict  { The Line }
    Output:
        answer      ->  String  { The Answer That Created By Details . }
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
    """
    A Simple Function To Remove All Spaces In A String.
    """
    tempString = ""
    for i in string.strip().split(" "):
        tempString += i
    return tempString

def euqals(string1,string2):
    """
    Checks If Two String Equals Together Or Not ( Without Any Space )
    """
    if removeSpace(string1) == removeSpace(string2):
        return True
    return False

def checkIfExists(text,string,line = 0):
    """
    Input :
        text       ->  String  { All Of The Text As An Array }
        string     ->  String  { The String That We Wanted To Find }
        line       ->  Int     { The Line That Function Will Check After This Line Number }
    Output:
        answer      ->  String  { The Answer That Created By Details . }
    Check That If A String Exists In a File Or Not ( After An Specific Line )
    """
    return smartIn(text[line:],string)


def isSW(code):
    """
    Input :
        code          ->  String  { The Code As A Big String }
    Output:
        True / False  ->  Bool  { Is It Simple Web Code ? }
    Checks If The Code Is A Simple Web Code Or Not.
    """
    start = re.findall("@[A-Za-z][A-Za-z]*",code)
    end = re.findall("@@[A-Za-z][A-Za-z]*",code)
    sok = 0
    eok = 0
    for i in start:
        if isHTML(i.replace("@","").strip()):
            sok += 1
    for i in end:
        if isHTML(i.replace("@@","").strip()):
            eok += 1
    if sok > (len(start) // 2) and eok > (len(end) // 4):
        return True
    return False
