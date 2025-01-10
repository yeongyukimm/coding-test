import json
from book import Book
from library import Library


def load_books_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        book_data = json.load(f)
    books = [Book(book['title'], book['author'], book['year'], book['isbn'], False) for book in book_data["book_list"]]
    return books


if __name__ == "__main__":

    books = load_books_from_file('book_list.json')
    library = Library(books)
    
    for book in books:
        library.add_book(book)

    library.find_book("Python")

    if books:
        first_book = books[0]
        first_book.print_info()
        first_book.borrow()
        first_book.print_info()
        first_book.return_book()
        first_book.print_info()

    library.delete_book(books[0].isbn)
    library.export_all_books()