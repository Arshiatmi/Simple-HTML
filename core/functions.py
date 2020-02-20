def file_replace(file_name,text,replace):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    lines = [i.replace(text,replace) for i in lines]
    file = open(file_name,"w")
    file.writelines(lines)
    file.close()
