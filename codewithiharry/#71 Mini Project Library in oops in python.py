from time import sleep


class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.lname = name
        self.lend_dict = {}

    def Display_Books(self):
        print(f"We Have These Books In Our {self.lname}Library:- ")
        for BOOK in self.bookslist:
            print(BOOK)

    def lend_book(self, user, book):
        if book not in self.lend_dict.values():
            self.lend_dict.update({book: user})
            print("Book Reserved For You.\nWe Will Diliver It To You in 1 hour\n")
        else:
            print(f"Book Taken By {self.lend_dict[book]}\nTry Later\n")

    def add_book(self, book):
        self.bookslist.append(book)
        print("Thank You For Donating Us Book\nOur Staff Will Reach Your Home to Take Book\n")

    def return_book(self, book):
        self.lend_dict.pop(book)
        print("Our Staff Will Take Book From You In Half Hour\n")


if __name__ == '__main__':
    library_name = input("Enter Your Library Name:- ")
    library_books = list(input("Enter Your Books Name:- ").lower())
    server = Library(["happy Rai Kothi", "its all Fine"], "Harry")
    while True:
        sleep(3)
        print("1 - Display All Books")
        print("2 - Lend The Boook ")
        print("3 - Add Book")
        print("4 - Return Book\n")
        user_choice = int(input("Enter Your Number of Choice:- "))

        if user_choice == 1:
            server.Display_Books()
            print()

        elif user_choice == 2:
            name = input("Enter Your Name:-").lower()
            book = input("Enter your Book Name:- ").lower()
            server.lend_book(name, book)

        elif user_choice == 3:
            bookname = input("Which book You Want To Donate:- ").lower()
            server.add_book(bookname)

        elif user_choice == 4:
            bookname = input("Which Book You want To Return:-").lower()
            server.return_book(bookname)

        else:
            print("Not A Valid option")
