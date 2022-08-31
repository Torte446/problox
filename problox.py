import os, sys
from time import sleep
import json
import keyboard
import string
import time
from colorama import Fore
from colorama import init as colorama_init
colorama_init()


probloxpath = os.getcwd().replace("\\", "/")
tweakspath = probloxpath+"/tweaks"
localappdata = os.getenv("LOCALAPPDATA").replace("\\", "/")

sys.path.insert(1, tweakspath)

problox = """
______          _     _           
| ___ \        | |   | |          
| |_/ / __ ___ | |__ | | _____  __
|  __/ '__/ _ \| '_ \| |/ _ \ \/ /
| |  | | | (_) | |_) | | (_) >  < 
\_|  |_|  \___/|_.__/|_|\___/_/\_\\ Vb0.2
                                 
"""

def setdata(key, value, file = "problox.json"):
    with open(file, "r") as f:
        cfg = json.loads(f.read())
        cfg[key] = value

    with open(file, "w") as f:
        f.write(json.dumps(cfg))

def getdata(key, file = "problox.json"):
    with open(file, "r") as f:
        try:
            cfg = json.loads(f.read())
            return cfg[key]
        except KeyError:
            return None

def listdirs(path):
    b = os.getcwd()
    os.chdir(path)
    r = [name for name in os.listdir(".") if os.path.isdir(name)]
    os.chdir(b)
    return r

def listfiles(path):
    b = os.getcwd()
    os.chdir(path)
    r = [name for name in os.listdir(".") if os.path.isfile(name)]
    os.chdir(b)
    return r

def listall(path):
    b = os.getcwd()
    os.chdir(path)
    r = [name for name in os.listdir(".")]
    os.chdir(b)
    return r

def find_roblox():
    path = f"{localappdata}/Roblox/Versions/"
    versions = listdirs(path)
    for ver in versions:
        p = path + ver
        files = listfiles(p)
        if "RobloxPlayerLauncher.exe" in files:
            return p.replace("\\", "/")
    
def find_robloxstudio():
    path = f"{localappdata}/Roblox/Versions/"
    versions = listdirs(path)
    for ver in versions:
        p = path + ver
        files = listfiles(p)
        if "RobloxStudioLauncherBeta.exe" in files:
            return p.replace("\\", "/")


roblox = find_roblox()
robloxstudio = find_robloxstudio()

if __name__ == "__main__":
    while True:
        print(problox)
        print("Enable/disable tweaks\n")
        rd = {}
        en = {}
        n = 0
        os.chdir("./tweaks")
        tweaks = listdirs(".")
        os.chdir(probloxpath)
        if len(tweaks) > 35:
            print("Tweak limit (35) exceeded! Please remove some tweaks and hit any button to continue.")
            os.system("pause >NUL")
            continue
            
        for name in tweaks:
            n += 1
            a = n
            if a > 9:
                a -= 9
                a = string.ascii_lowercase[a]
            rd[str(a)] = name
            enabled = getdata("enabled", "tweaks/"+name+"/config.json")
            if enabled == True:
                en[name] = True
                print(Fore.GREEN + f"[{str(a)}] " + Fore.RESET + name)
            else:
                en[name] = False
                print(Fore.LIGHTRED_EX + f"[{str(a)}] " + Fore.RESET + name)
        tweak = "sdwr"
        while not tweak in rd.keys():
            tweak = keyboard.read_key()
        tweak = rd[tweak]
        
        en[tweak] = not en[tweak]
        
        exec("import "+tweak+" as t_current")

        os.chdir(f"{probloxpath}/tweaks/{tweak}")
        exec(f"t_current.set_state({en[tweak]}, \"{probloxpath}\", \"{roblox}\", \"{robloxstudio}\")")
        os.chdir(probloxpath)

        time.sleep(0.5)
        setdata("enabled", en[tweak], "tweaks/"+name+"/config.json")
        os.system("cls")
