class Library:
    file = "books.txt"
    list = []
    def __init__(self): #constructor method
        self.file = open("books.txt", "r+") #"a+" did not work for me. So I used "r+".
    def __del__(self): #NOT-COMPLETE
        self.file.close()

    def listBooks(self):
        lines = self.file.read().splitlines()
        for elt in lines:
            print("book:",elt.split(",")[0],", author:",elt.split(",")[1])   

    def addBook(self):
        title = input("Please enter book title:")
        author = input("Please enter book author:")
        year = input("Please enter first release year:")
        numOfPage = input("Please enter number of pages:")

        newLine = title + "," + author + "," + year + "," + numOfPage + "\n"

        self.file.write(newLine)

    def removeBook(self):
        title = input("Please enter the book title you want to delete:")
        lines = self.file.read().splitlines()
        print(lines)
        for i in range(len(lines)):
            if(lines[i].split(",")[0] == title):
                 lines.remove(i)
        self.file.truncate(0)
        for elt in lines:
            self.file.write(elt+"\n")


myLib = Library()
myLib.listBooks()
# myLib.addBook()
# myLib.addBook()
# myLib.addBook()
print(myLib.file.read())
myLib.removeBook()

