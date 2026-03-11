from Book import Book
from Library import Library, FastLibrary

book1 = Book("1984", "George Orwell", 1949, "Distopia")
book2 = Book("Il nome della rosa", "Umberto Eco", 1980, "Storico")
book3 = Book("Orgoglio e pregiudizio", "Jane Austen", 1813, "Romanzo")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

print("\n--- Searching for Totti's books ---")
try:
    for book in library.find_books_by_author("Totti"):
        print(book)
except ValueError as e:
    print(e)

print("\n--- Searching for books published in 1980 ---")
try:
    for book in library.find_books_by_year(1980):
        print(book)
except ValueError as e:
    print(e)