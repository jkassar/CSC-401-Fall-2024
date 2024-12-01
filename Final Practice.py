class Book:
    def __init__(self,title,author,pgnum=0,checked_out = 'No'):
        self.t = title
        self.a = author
        self.n = pgnum
        self.c = checked_out

    def __repr__(self):
        return f'Book ({self.t}, {self.a})'

    def available(self):
        if self.c == 'No':
            return True
        if self.c == 'Yes':
            return False
    def modavailability(self,status = 'Yes'):
        self.c = status

def checkout_book(title, author):
    my_book = Book(title, author)
    if book.available():
        book.modavailability()
    return repr(book)



