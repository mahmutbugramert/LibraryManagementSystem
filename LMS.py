class Library:
    file = None
    def __init__(self): #constructor method
        self.file = open("books.txt", "a+") 

    def __del__(self): #destructor method
        self.file.close()

    def listBooks(self):
        self.file.seek(0)
        myFile = self.file.read()
        lines = myFile.splitlines()
        if(len(lines) == 0):
            print("------------------\nNo book in databese!\n------------------")
        else:
            print("------------------")
            for elt in lines:
                print("book:",elt.split(",")[0],", author:",elt.split(",")[1])
            print("------------------")

    def addBook(self):
        self.file.seek(0)
        title = input("Please enter book title:")
        author = input("Please enter book author:")
        year = input("Please enter first release year:")
        numOfPage = input("Please enter number of pages:")

        newLine = title + "," + author + "," + year + "," + numOfPage + "\n"

        self.file.seek(0, 2)
        self.file.write(newLine)
        
    def removeBook(self):
        self.file.seek(0)
        title = input("Please enter the book title you want to delete:")
        myFile = self.file.read()
        lines = myFile.splitlines()
        flag = True
        for i in range(len(lines)):
            if(lines[i].split(",")[0] == title):
                 flag = False
                 lines.pop(i)
                 break
        if(flag):
            print("----------------------\nNo book named", title, "in the database!\n----------------------")
        self.file.seek(0)
        self.file.truncate(0)
        for elt in lines:
            self.file.write(elt+"\n")


lib = Library()

print("Welcome to the Library Management System!")
while True:
    operation = input("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Exit\n")
    if(operation == "1"):
        lib.listBooks()
    elif(operation == "2"):
        lib.addBook()
    elif(operation == "3"):
        lib.removeBook()
    elif(operation == "4"):
        break
    else:
        print("------------------------------\nUnrecognised input. Try again!\n------------------------------")

