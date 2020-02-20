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
