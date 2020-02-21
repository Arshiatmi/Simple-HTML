from core.error_handler import *
from core.functions import *

def deepTranslate(code):
    """
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

    # Do Deep Translations
    code = deepTranslate(code)

    return code
