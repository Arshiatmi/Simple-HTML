from core.error_handler import *
from core.functions import *

def checkForWarnings(code):
    """
    Input :
        code  ->  Array { The Code }
    Output:
        null
    This Function Will Give Some Common Warnings. For Example :
        -> @head
          It Seems You Forgot To Close Your Tag !
    """
    for c,i in enumerate(code):
        tags = getAllTags(i)
        start = tags["start"]
        end = tags["end"]
        start.sort()
        end.sort()
        okStarts = []
        for x in start:
            allProps = getProps(x,code,c)
            tg = allProps["_tagname"]
            okStarts.append(tg)
        start = okStarts
        for j in start:
            ok = False
            for z in end:
                if "@@" + j == z:
                    ok = True
            if not ok:
                if not checkIfExists(code,"@" + j,c):
                    createWarning("Tag Parsing",f"The Tag {j} Opened But Not Closed !",code,c)
            ok = False


def deepTranslate(code):
    """
    Input :
        code  ->  String  { Full Code }
    Output:
        code  ->  String  { Translated Code }
    This Function Will Translate With Properties. For Example :
        @body( #myid , $myname , bgcolor => "black" )
    Will Return :
        <body id="myid" name="myname" bgcolor="black">
    """
    for c,i in enumerate(code):
        tags = getAllTags(i)
        for j in tags["end"]:
            code[c] = code[c].replace(j,"</" + j.replace("@@","") + ">")
        for j in tags["start"]:
            tagDetails = getProps(j,code,c)
            tag = createHTMLTag(tagDetails)
            code[c] = code[c].replace(j,tag)
    return code

def translate(code):
    """
    Compile The Code That Passed As A List.
    """
    # Open Repos ( Get Keywords From Repo Files)
    repos_handler = open("repos/html.txt")
    keywords = [i.replace("\n","") for i in repos_handler.readlines()]
    repos_handler.close()

    # Check Warnings
    checkForWarnings(code)

    # Do Deep Translations
    code = deepTranslate(code)

    return code
