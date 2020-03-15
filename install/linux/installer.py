import sys
sys.path.append("../../core/")
from color import setColorF
import os

tar = "/usr/bin/python3"
print(f"""Is Your Python Address Is {setColorF(tar.replace("#!","").strip(),"green")} ?  
If You Dont Know What Is It, You Run Python Like {setColorF('1',"yellow")}:{setColorF('python3 file.py',"green")} Or {setColorF('2',"yellow")}:{setColorF('python file.py',"green")} ?
 * {setColorF('Case 1',"green")} : {setColorF("Just Write '1' Then Press Enter / Press Enter.","yellow")}
   {setColorF('Case 2',"green")} : Just Write '2' Then Press Enter.
   {setColorF('Case 3',"green")} : Write The Address Then Press Enter.
""")
while True:
    x = input(f"""( {setColorF('1',"yellow")} Is Default ) : """)
    if x.strip() == "1":
        break
    elif x.strip() == "2":
        if os.path.exists("/usr/bin/python"):
            tar = "/usr/bin/python"
            break
        else:
            print("Sorry Path Not Found :( ")
    else:
        if x.startswith("#!"):
            x = x[2:].strip()
        if os.path.exists(x.strip()):
            tar = x.strip()
            break
        else:
            print("Sorry Path Not Found :( ")
tar = "#! " + tar
def say(string,bad=False):
    if bad:
        print(setColorF(string,"red"))
    else:
        print(setColorF(string,"green"))

print("\n\n")
say("[+] Lets Copy :) Getting Target From $PATH Linux Variable ")
path = os.popen("echo $PATH").read()
target = ""
if "/usr/bin" in path:
    say("\t[+] /usr/bin Selected .")
    target = "/usr/bin"
else:
    options = path.split(":")
    for c,i in enumerate(options):
        print(f"\t\t[{c + 1}] : {i}")
    print()
    target = options[int(input("\tEnter Which One Should Be Target : ")) - 1]
    say(f"\t[+] {target} Selected .")
answer = os.popen(f"""cp ../../sw.py {target}/sw
cp -r ../../core {target}
cp -r ../../repos {target}""").read()
if "error" not in answer.lower():
    say("\t[+] Copied :)")
    say("[+] Preparing... ")
    string = f""" echo "{tar}"; cat {target}/sw; """
    os.popen("{" + string + "} " + f">{target}/sw.tmp").read()
    os.popen(f"mv {target}/sw.tmp {target}/sw").read()
    os.popen(f"chmod +x {target}/sw").read()
    say("[+] Seems Installed :)")
    print(setColorF("Let's Have Fun Now :)","yellow"))
else:
    say("[-] Sorry Seems Some Error Happend :(((",True)
    


