import time
import random

from Book import Book
from Library import Library, FastLibrary

library = Library()
library_fast = FastLibrary()

print("building Library and FastLibrary...")

for i in range(100000):
    title = f"Book{i}"
    author = f"Author{i}"
    year = 2000 + (i % 25)
    genre = f"Genre{24-(i % 25)}"

    new_book = Book(title, author, year, genre)
    library.add_book(new_book)
    library_fast.add_book(new_book)

print("Library completed, total len:", len(library.books))
print("FastLibrary completed, total len:", len(library_fast.books))

n_ricerche = 1000
print(f"\nNumber of random search: {n_ricerche}")

author_to_search = []
for i in range(n_ricerche):
    ran = random.randint(0, 99999)
    author_to_search.append(f"Author{ran}")

print(f"Starting searching in Library: ........")

t_start = time.time()
for a in author_to_search:
    try:
        res = library.find_books_by_author(a)
    except ValueError:
        pass
t_end = time.time()
t_tot = t_end - t_start

print("Finished!!!!")
print(f"Total time: {t_tot:.10f} sec\n")


print(f"Starting searching in FastLibrary: ........")

tf_start = time.time()
for a in author_to_search:
    try:
        res = library_fast.find_books_by_author(a)
    except ValueError:
        pass
tf_end = time.time()
tf_tot = tf_end - tf_start

print("Finished!!!!")
print(f"Total time: {tf_tot:.10f} sec\n")
