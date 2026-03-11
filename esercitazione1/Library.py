from Book import Book

class Library :
    def __init__(self) :
        self.books = []

    def add_book(self, book) :
        self.books.append(book)

    def remove_book(self, book) :
        if book in self.books:
            self.books.remove(book)
        else :
            raise ValueError(f"*{book}* not in library")
        
    def show_books(self):
        print("Books in Library:")
        for book in self.books:
            print(book)

    def find_books_by_author(self, author):
        res = []

        for book in self.books:
            if book.author == author:
                res.append(book)
        if not res: 
            raise ValueError(f"*{author}* 's book not in library")
        return res
    
    def find_books_by_year(self, year) :
        res = []

        for book in self.books:
            if book.year == year:
                res.append(book)
        if not res: 
            raise ValueError(f"*{year}* 's book not in library")
        return res
    
class FastLibrary(Library) :
    def __init__(self) :
        super().__init__()
        self.author_index = {}
        self.year_index = {}

    def add_book(self, book) :
        super().add_book(book)
        if book.author not in self.author_index:
            self.author_index[book.author] = []
        self.author_index[book.author].append(book)
        if book.year not in self.year_index:
            self.year_index[book.year] = []
        self.year_index[book.year].append(book)

    def remove_book(self, book):
        super().remove_book(book)
        if book.author in self.author_index and book in self.author_index[book.author]:
            self.author_index[book.author].remove(book)
            if not self.author_index[book.author]:
                del self.author_index[book.author]
        if book.year in self.year_index and book in self.year_index[book.year]:
            self.year_index[book.year].remove(book)
            if not self.year_index[book.year]:
                del self.year_index[book.year]

    def find_books_by_author(self, author):
        res = self.author_index.get(author, [])
        if not res: 
            raise ValueError(f"*{author}* 's book not in library")
        return res        
    
    def find_books_by_year(self, year):
        res = self.year_index.get(year, [])
        if not res: 
            raise ValueError(f"*{year}* 's book not in library")
        return res

