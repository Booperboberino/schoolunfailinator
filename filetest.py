import os
def ensureFoldersExist(fileLocation):
    a = fileLocation.split('/')
    for i in range(len(a)-1):
        path = ""
        for j in range(0,i+1):
            path+=a[j] +"/"
        #print(path[len(path)-5:])
        if not os.path.exists(path):
            os.mkdir(path)
string = '2021/4/20.txt'
ensureFoldersExist(string)        
f = open(string,'a')
f.write("testing")
f.close()