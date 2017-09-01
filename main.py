import os
import getpass

from Main import EditFile as EF

chatFile = "P:/Composite/All Students/Chat.txt"
nameFile = "U:/Name.txt"
name = None
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def RemoveNumbers(Str):
    newStr = ""
    r = False
    
    for x in Str:
        for num in numbers:
            if str(num) == x:
                r = True
                break
        if r:
            r = False
        else:
            newStr += x
    return newStr
        

def Setup():
    global name
    
    if not EF.TestFile(chatFile):
        File = open(chatFile, "w")
        File.close()
    
    tName = getpass.getuser()
    tName = tName.split(".")
    name = tName[0].Capitalize() + " " + RemoveNumbers(tName[1].Capitalize())
    
if __name__ == "__main__":
    Setup()
