class loader():


    # __init__(self):

    # Loads every date 
    def loadAllDates(self):
        with open("txt/testdata.txt", "r") as fp:
            for i in fp:
                print(i)
        return "a"


with open("txt/testdata.txt", "r") as fp:
    cnt = 0
    for i in fp:
        # do
        ""
