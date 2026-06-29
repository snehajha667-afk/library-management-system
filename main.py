class Library:
    def __init__(self):
        self.book = "Python"

    def show_book(self):
        print("Book in library:", self.book)

    def issue_book(self):
        print(self.book, "has been issued.")

    def return_book(self):
        print(self.book, "has been returned.")


obj = Library()

obj.show_book()
obj.issue_book()
obj.return_book()
