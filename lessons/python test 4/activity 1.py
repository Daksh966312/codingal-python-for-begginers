class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"'{self.title}' by {self.author} has been brrowed")

    def return_book(self):
        self.is_borrowed = False
        print(f"'{self.title}' by '{self.author}' has been returned")

book1 = Book("Harry Potter", "JK Rowling")
book2 =  Book("1984", "George Orwell")
book3 = Book("How to kill a mockingbird", "Harper Lee")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()