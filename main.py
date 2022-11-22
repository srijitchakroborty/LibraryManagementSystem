class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("The books present in the library are: ")
        for book in self.books:
            print("\t*",book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. You will need to return it in 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("The book is not available currently.")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print(f"Thanks for returning {bookName}. Hope you enjoyed reading it.")

class Student:
    def requestBook(self):
        self.book=input("Enter the name of the book you want to borrow. Please type it as it is in the list:\t")
        return self.book

    def returnBook(self):
        self.book=input("Enter the name of the book you want to return or add:\t")
        return self.book

if __name__ == '__main__':
    centralLibrary=Library(["All about Python","Macbeth","Death on nile","Advance C++","Sherlock Holmes short stories", "Nemesis", "The Great Gatsby", "Jane Eyre", "War and Peace", "A Passage to India", "My Expirements with Truth"])
    stu=Student()

    welcomeMsg='''\n====Welcome to Central Library====
    Please choose an option:
    1. List of available books
    2. Request a book
    3. Return/Add a book
    4. Exit the library system
    '''
    print(welcomeMsg)
    while(True):
        print("Press 1 to view available books, 2 to request a book, 3 to return or add a book and 4 to exit the library system\n")
        try:
            a=int(input("Enter your choice: "))
            if a==1:
                centralLibrary.displayAvailableBooks()
            elif a==2:
                centralLibrary.borrowBook(stu.requestBook())
            elif a==3:
                centralLibrary.returnBook(stu.returnBook())
            elif a==4:
                print("Thanks for using.")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Invalid input. Please type 1 or 2 or 3 or 4.")
