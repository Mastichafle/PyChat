import os

from Main import EditFile as EF

chatFile = "P:/Composite/All Students/Chat.txt"
nameFile = "U:/Name.txt"
name = ""

def Setup():
    global name
    
    if not EF.TestFile(chatFile):
        File = open(chatFile, "w")
        File.close()
   
    #if not EF.TestFile(nameFile):
        #while Name == "":
            
    
if __name__ == "__main__":
    Setup()
