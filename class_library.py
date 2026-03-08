#class library ; book name, author, availability . mehtods - check out a book, return a book, display available books 
class Library:
    def __init__(self, name, author,  avail):
        self.name  = name
        self.author = author
        self.avail = avail
    
    def checkout(self):
        if self.avail:
            self.avail = False
            print (f"Book : {self.name} by {self.author} has been checked out.")

        else :
            print (f"Book : {self.name} by {self.author} is unavaialble.")

    def return_book(self) :
        if not self.avail:
            self.avail = True
            print (f"Book : {self.name} by {self.author} has been returned.")
        else :
            print (f"Book : {self.name} by {self.author} was not checked out.")
    
    def display(self):
        status = "Available" if self.avail else "checked out"
        print (f"Book : {self.name} by {self.author} is {status}")

librarybooks = [
    Library("1234", "hfiiewj"),
    Library("6484", "jyaei"),
    Library("jdshoiw", "uiodj")
]

while True:
    print ("\n 1. Chceck Out Book \n 2. Return Book \n 3. Check Availability \n 4. Exit")
    choice = int(input("Enter your choice:  "))
    