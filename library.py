# import pandas as pd
import csv
from book import Book


class Library(Book):
    def __init__(self, books):
        self.books = books
        
    def add_book(self, Book):
        self.books.append(Book.title)
        print(f"'{Book.title}'이(가) 도서 목록에 추가되었습니다.")

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"ISBN {isbn}인 도서가 삭제되었습니다.")
        print(f"ISBN {isbn}인 도서를 찾을 수 없습니다.")

    def find_book(self, keyword):
        results = [book for book in self.books if keyword in (book.title, book.author, book.isbn)]
        if results:
            print(f"'{keyword}'에 대한 검색 결과:")
            for book in results:
                book.print_info()
        else:
            print(f"'{keyword}'에 대한 결과가 없습니다.")
        return results

    def export_all_books(self, filename="library_books.csv"):
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Author", "Year", "ISBN", "Is Borrowed"])
            for book in self.books:
                writer.writerow([book.title, book.author, book.year, book.isbn, book.is_borrowed])
        print(f"도서 목록이 '{filename}'로 저장되었습니다.")