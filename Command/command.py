import time


class Book:
    _instances = []

    def __init__(self, title: str) -> None:
        self.title = title
        self.rating = 0
        Book._instances.append(self)

    def rate(self, star: int) -> None:
        self.rating = star


class BookService:
    def get_all_books(self) -> list:
        return Book._instances

    def get_book_by_title(self, title: str) -> Book:
        for book in Book._instances:
            if book.title == title:
                return book
    
    def rate(self, title: str, star: int) -> Book:
        book = self.get_book_by_title(title)
        book.rate(star)
        return book


class CommandInterface:
    service = BookService()

    def get_service(self):
        return self.service


class ListCommand(CommandInterface):
    def execute(self):
        return self.get_service().get_all_books()


class RetrieveCommand(CommandInterface):
    def execute(self, title):
        return self.get_service().get_book_by_title(title)


class RateCommnad(CommandInterface):
    def execute(self, title, star):
        return self.get_service().rate(title, star)


class BookView:
    def __init__(self) -> None:
        self.list_cmd = ListCommand()
        self.retieve_cmd = RetrieveCommand()
        self.rate_cmd = RateCommnad()
    
    def list(self) -> None:
        books = self.list_cmd.execute()
        for book in books:
            print(book.title)

    def retrieve(self) -> None:
        title = input("책 제목을 입력하세요: ")
        time.sleep(1.5)
        book = self.retieve_cmd.execute(title)
        print(f'{book.title}을 가져왔습니다.')

    def rate(self) -> None:
        title = input("책 제목을 입력하세요: ")
        star = input("평점을 입력하세요: ")
        time.sleep(1.5)
        book = self.rate_cmd.execute(title, star)
        print(f'{book.title}의 평점이 {book.rating}점으로 변경되었습니다.')


def main():
    book1 = Book(title='The Little Prince')
    book2 = Book(title='Harry Potter')

    view = BookView()
    print("모든 책을 가져옵니다.")
    time.sleep(1.5)
    view.list()
    time.sleep(1.5)
    print("제목으로 책을 검색합니다.")
    view.retrieve()
    time.sleep(1.5)
    print("책의 평점을 변경합니다.")
    view.rate()


main()
