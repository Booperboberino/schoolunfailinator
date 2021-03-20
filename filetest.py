import os #imports os
def ensureFoldersExist(fileLocation): #function that I haven't tested cause I didn't have it in function form in IDLE, checks for folders of .txt and creates them if they don't exist to prevent error
    a = fileLocation.split('/')
    for i in range(len(a)-1): #goes through all the different folders, but not the file
        path = ""
        for j in range(0,i+1): #assembles the path
            path+=a[j] +"/"

        if not os.path.exists(path): #creates folder if it doesn't exist
            os.mkdir(path)

#just some code that I had to test it out
string = '2021/4/20.txt' #file corresponding to the data of 4/20/2021
ensureFoldersExist(string)        
f = open(string,'a') #opens or creates the file
f.write("testing") 
f.close()