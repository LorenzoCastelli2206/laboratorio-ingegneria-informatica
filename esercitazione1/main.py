from Book import Book
from Library import FastLibrary

def main() :
    libreria = FastLibrary()

    #Libreria popolata da gemini per testare il programma
    libreria.add_book(Book("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, "Fantasy"))
    libreria.add_book(Book("1984", "George Orwell", 1949, "Dystopian"))
    
    # Isaac Asimov (Sci-Fi)
    libreria.add_book(Book("Fondazione", "Isaac Asimov", 1951, "Sci-Fi"))
    libreria.add_book(Book("Fondazione e Impero", "Isaac Asimov", 1952, "Sci-Fi"))
    libreria.add_book(Book("Seconda Fondazione", "Isaac Asimov", 1953, "Sci-Fi"))
    libreria.add_book(Book("Io, Robot", "Isaac Asimov", 1950, "Sci-Fi"))
    libreria.add_book(Book("L'orlo della Fondazione", "Isaac Asimov", 1982, "Sci-Fi"))
    libreria.add_book(Book("Nemesis", "Isaac Asimov", 1989, "Sci-Fi"))

    # Stephen King (Horror / Fantasy)
    libreria.add_book(Book("Shining", "Stephen King", 1977, "Horror"))
    libreria.add_book(Book("It", "Stephen King", 1986, "Horror"))
    libreria.add_book(Book("Misery", "Stephen King", 1987, "Horror"))
    libreria.add_book(Book("Pet Sematary", "Stephen King", 1983, "Horror"))
    libreria.add_book(Book("Carrie", "Stephen King", 1974, "Horror"))
    libreria.add_book(Book("Il miglio verde", "Stephen King", 1996, "Fantasy"))

    # Agatha Christie (Mystery)
    libreria.add_book(Book("Dieci piccoli indiani", "Agatha Christie", 1939, "Mystery"))
    libreria.add_book(Book("Assassinio sull'Orient Express", "Agatha Christie", 1934, "Mystery"))
    libreria.add_book(Book("La serie infernale", "Agatha Christie", 1936, "Mystery"))
    libreria.add_book(Book("Poirot a Styles Court", "Agatha Christie", 1920, "Mystery"))
    libreria.add_book(Book("L'assassinio di Roger Ackroyd", "Agatha Christie", 1926, "Mystery"))

    # J.K. Rowling (Fantasy / Thriller)
    libreria.add_book(Book("Harry Potter e la Pietra Filosofale", "J.K. Rowling", 1997, "Fantasy"))
    libreria.add_book(Book("Harry Potter e la Camera dei Segreti", "J.K. Rowling", 1998, "Fantasy"))
    libreria.add_book(Book("Harry Potter e il Prigioniero di Azkaban", "J.K. Rowling", 1999, "Fantasy"))
    libreria.add_book(Book("Harry Potter e il Calice di Fuoco", "J.K. Rowling", 2000, "Fantasy"))
    libreria.add_book(Book("Harry Potter e l'Ordine della Fenice", "J.K. Rowling", 2003, "Fantasy"))
    libreria.add_book(Book("Harry Potter e il Principe Mezzosangue", "J.K. Rowling", 2005, "Fantasy"))
    libreria.add_book(Book("Harry Potter e i Doni della Morte", "J.K. Rowling", 2007, "Fantasy"))
    libreria.add_book(Book("Il seggio vacante", "J.K. Rowling", 2012, "Thriller"))

    # Ursula K. Le Guin (Fantasy / Sci-Fi)
    libreria.add_book(Book("Il mago di Earthsea", "Ursula K. Le Guin", 1968, "Fantasy"))
    libreria.add_book(Book("Le tombe di Atuan", "Ursula K. Le Guin", 1971, "Fantasy"))
    libreria.add_book(Book("La spiaggia più lontana", "Ursula K. Le Guin", 1972, "Fantasy"))
    libreria.add_book(Book("I reietti dell'altro pianeta", "Ursula K. Le Guin", 1974, "Sci-Fi"))
    libreria.add_book(Book("La mano sinistra della tenebra", "Ursula K. Le Guin", 1969, "Sci-Fi"))


    while True:
        print("\n" + "=====================================")
        print("--- MENU PRINCIPALE ---")
        print("1. Visualizza tutti i libri")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca libri per autore")
        print("4. Cerca libri per anno")
        print("5. Rimuovi un libro")
        print("6. Esci")
        print("=====================================")

        scelta = input("\nScegli da 1 a 6: ")

        if scelta == '1':
            libreria.show_books()

        elif scelta == '2':
            print("\nAggiungo il libro")
            titolo = input("Titolo: ")
            autore = input("Autore: ")
            try:
                anno = int(input("Anno di pubblicazione: "))
            except ValueError:
                print("INSERIRE UN INTERO")
                continue
            genere = input("Genere: ")

            new_book = Book(titolo, autore, anno, genere)
            libreria.add_book(new_book)
            print("Libro aggiunto")

        elif scelta == '3':
            print("\nRicerca per AUTORE")
            autore = input("Autore: ")
            try:
                res = libreria.find_books_by_author(autore)
                print("Sono stati trovati:")
                for libro in res:
                    print(f"---{libro}")
            except ValueError as e:
                print(f"\n{e}")

        elif scelta == '4':
            print("\nRicerca per ANNO")
            try:
                anno = int(input("Anno: "))
            except ValueError:
                print("INSERIRE UN INTERO")
                continue
            try:
                res = libreria.find_books_by_year(anno)
                print("Sono stati trovati:")
                for libro in res:
                    print(f"---{libro}")
            except ValueError as e:
                print(f"\n{e}")

        elif scelta == '5':
            print("\nRimozione Libro")
            titolo = input("Titolo: ")
            autore = input("Autore: ")
            libro_da_rimuovere = None
            for book in libreria.books:
                if book.title == titolo and book.author == autore:
                    libro_da_rimuovere = book
                    break
            if libro_da_rimuovere:
                try:
                    libreria.remove_book(libro_da_rimuovere)
                    print("Libro rimosso")
                except ValueError as e:
                    print(f"\n{e}")
            else:
                print("\nIl libro non è presente!")

        elif scelta == '6':
            print("\nUscita dal programma...")
            break

        else: 
            print("\nopzione non valida. Scegli da 1 a 7: ")

if __name__ == "__main__":
    main()