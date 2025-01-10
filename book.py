class Book():
    def __init__(self, title, author, year, isbn, is_borrowed):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def print_info(self):
        status = "대출 중" if self.is_borrowed else "대출 가능"
        print(f"제목: {self.title}, 저자: {self.author}, 출판연도: {self.year}, ISBN: {self.isbn}, 상태: {status}")

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}'이(가) 대출되었습니다.")
        else:
            print(f"'{self.title}'은(는) 이미 대출 중입니다.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}'이(가) 반납되었습니다.")
        else:
            print(f"'{self.title}'은(는) 대출 상태가 아닙니다.")