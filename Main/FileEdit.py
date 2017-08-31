import os

def ReadFile(File):
    try:
        File = open(File, "r")
        File.close()
    except:
        return None
    
    try:
        File = open("Chat.txt", r)
        File.close()
        
        os.remove("Chat.txt")
        os.system("xcopy '"+File+"'")
    except:
        os.system("xcopy '"+File+"'")
    
    with open("Chat.txt", "r") as File:
        lines = File.readlines()
    
    return lines

def WriteFile(File, Data):
    while 1:
        try:
            with open(File, "w") as File:
                File.write(Data)
            break
        except:
            continue
