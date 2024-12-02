from typing import List
import json

class Book:
    # ობიექტის ატრიბუტების ინიციალიზაცია
    def __init__(self, title: str, author: str, published_in: int):
        self._title = title.strip()
        self._author = author.strip()
        self._published_in = published_in

    # დიქტად გადაქცევის მეთოდი
    def convert_to_dict(self) -> dict:
        return {
            'title': self._title,
            'author': self._author,
            'published_in': self._published_in,
        }

    # Book-ის ტიპად გადაქცევის მეთოდი
    @staticmethod
    def from_dict_to_book(data):
        return Book(data['title'], data['author'], data['published_in'])

    def __str__(self) -> str:
        return f"'{self._title}' by {self._author}, published in {self._published_in}"

class BookManager:
    def __init__(self):
        # წიგნების ცარიელი სია
        self._books: List[Book] = []

    def _is_duplicate(self, new_book: Book) -> bool:
        # იტერაცია წიგნებზე
        for book in self._books:
            # თუ წიგნის სათაური გადაწოდებული წიგნის სათაურის იდენტურია
            if book._title == new_book._title:
                # დავაბრუნებთ True-ს (ანუ დუბლიკატი არსებობს)
                return True
        # თუ არა, მაშინ დავაბრუნებთ False-ს(დუბლიკატი არ არსებობს)
        return False

    def add_book(self, book: Book) -> None:
        # თუ წიგნებში გადაწოდებული წიგნის დუბლიკატი არსებობს
        if self._is_duplicate(book):
            # დავპრინტავთ:
            print(f"Book '{book._title}' already exists in the list.")
            # და მეთოდიდან გამოვალთ
            return
        # თუ გადაწოდებულ წიგნს დუბლიკატი არ ჰყავს
        else:
            # მაშინ წიგნთა სიაში დავამატებთ
            self._books.append(book)
            print(f"Book '{book._title}' was added.")

    def display_books(self) -> None:
        # თუ წიგნთა სია ცარიელია
        if not self._books:
            # დავპრინტავთ:
            print("Book list is empty.")
            # და მეთოდიდან გამოვალთ
            return
        print("\nBooks in the collection:")
        print("-" * 30)
        # წიგნების სიას გადავატარებთ
        for book in self._books:
            # და დავპრინტავთ თითოეულ წიგნს
            print(book)

    def find_books(self, title: str) -> None:
        # გადაწოდებულ სახელს ჩამოვაშორებთ არასასურველ სპეისებს და დაბალ რეგისტრში გადავიყვანთ
        title = title.strip().lower()
        # ჯერ გადავატარებთ წიგნების სიას და შემდეგ დავაბრუნებთ იმ წიგნს, რომლის 
        # სათაურიც ემთხვევა გადაწოდებულ სათაურს
        matching_books = [book for book in self._books if title in book._title.lower()]
        # თუ matching_books ცარიელია
        if not matching_books:
            # დავპრინტავთ, რომ წიგნი გადაწოდებული სათაურით ვერ მოიძებნა
            print(f"No books found containing the title '{title}'.")
        # თუ არა
        else:
            print(f"Books matching '{title}':")
            # გადავატარებთ matching_books
            for book in matching_books:
                # და დავპრინტავთ თითოეულ წიგნს
                print(book)

    def remove_book(self, title: str) -> None:
        # გადაწოდებულ სახელს ჩამოვაშორებთ არასასურველ სპეისებს და დაბალ რეგისტრში გადავიყვანთ
        title = title.strip().lower()
        # თავიდან წასაშლელი წიგნი იქნება None
        book_to_remove = None
        # შემდეგ გადავატარებთ წიგნთა სიას
        for book in self._books:
            # თუ წიგნის სათაური ემთხვევა გადაწოდებულ სათაურს
            if book._title == title:
                # წასაშლელი წიგნი იქნება ეგ წიგნი
                book_to_remove = book
                # და ლუპიდან გამოვალთ
                break
        # თუ წასაშლელი წიგნი არსებობს
        if book_to_remove:
            # წიგნთა სიიდან ამოვშლით
            self._books.remove(book_to_remove)
            print(f"Book '{title}' has been removed.")
        # თუ წასაშლელი წიგნი არ არსებობს
        else:
            print(f"Book with title '{title}' was not found.")

    def save_books_to_file(self, filename: str = 'Console Apps/books.json') -> None:
        # ვცდით შემდეგ ლოგიკას
        try:
            # გადაწოდებულ ფაილს წინიდან დავუმატებთ 'Console Apps/',
            # რათა მოქმედ დირექტორიაში შეინახოს
            local_filename = 'Console Apps/' + filename
            # გავხსნით ამ ფაილს
            with open(local_filename, "w") as file:
                # თითოეულ წიგნს გადავაქცევთ დიქტად და json ფორმატით "ჩავყრით" ამ ფაილში
                json.dump([book.convert_to_dict() for book in self._books], file, indent=4)
                print(f"Books saved to {local_filename}.")
        # და თუ პროგრამამ ფაილი ვერ იპოვა
        except FileNotFoundError:
            print("You didn't put correct path for a file")
    
    def load_books_from_file(self, filename: str) -> None:
        try:
            local_filename = 'Console Apps/' + filename
            with open(local_filename, "r") as file:
                # json ფაილიდან მონაცემების ამოტვირთვა
                data = json.load(file)
                # მონაცემების გადაყვანა Book ტიპად და წიგნთა სიაში დამატება
                self._books = [Book.from_dict_to_book(book_data) for book_data in data]
            # წარმატებული ჩატვირთვის შემთხვევაში ვბეჭდავთ შეტყობინებას
            print(f"Books loaded from {local_filename}.")
        # თუ ფაილი არ მოიძებნა, ვამუშავებთ FileNotFoundError-ს 
        except FileNotFoundError:
            print(f"File {local_filename} not found.")
        # თუ json ფაილში მონაცემები არასწორია, ვამუშავებთ ValueError-ს
        except ValueError:
            print("Invalid data in file.")

    @staticmethod
    def validate_book_data(title: str, author: str, published_in: int) -> bool:
        # თუ სათაური ცარიელია ან სტრინგის ტიპის არაა
        if not title or not isinstance(title, str):
            # დავპრინტავთ ერორს
            print("Invalid name! It must be a non-empty string.")
            # და დავაბრუნებთ False-ს
            return False
        # თუ ავტორის სახელი ცარიელია ან სტრინგის ტიპის არაა
        if not author or not isinstance(author, str):
            # დავპრინტავთ ერორს
            print("Invalid author! It must be a non-empty string.")
            # და დავაბრუნებთ False-ს
            return False
        # თუ გამოშვების წელი ცარიელია ან ინტეჯერის ტიპის არაა
        if not isinstance(published_in, int) or published_in <= 0:
            # დავპრინტავთ ერორს
            print("Invalid year! It must be a positive integer.")
            # და დავაბრუნებთ False-ს
            return False
        # თუ ყველა if blocks-ს გასცდა (ანუ ყველაფერი ვალიდურია)
        # დავაბრუნებთ True-ს
        return True
    
    def validate_and_add_book(self):
        name = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter year of publication: ")
        try:
            year = int(year)
            if BookManager.validate_book_data(name, author, year):
                self.add_book(Book(name, author, year))
        except ValueError:
            print("Invalid year! Please enter a valid integer.")

# მთავარო ფუნქცია, რომელიც დაწერილ ლოგიკას შეამოწმებს
def main():
    manager = BookManager()
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Display books")
        print("3. Find books by title")
        print("4. Remove a book")
        print("5. Save books to file")
        print("6. Load books from file")
        print("7. Exit")

        choice = input("Enter your choice: ")
        # მთავარი ფუნქციონალი და choice-ს შემოწმება
        match choice:
            case "1":
                manager.validate_and_add_book()
            case "2":
                manager.display_books()
            case "3":
                name = input("Enter book title to search for: ")
                manager.find_books(name)
            case "4":
                name = input("Enter book title to remove: ")
                manager.remove_book(name)
            case "5":
                filename = input("Enter filename to save books: ").strip()
                manager.save_books_to_file(filename)
            case "6":
                filename = input("Enter filename to load books: ").strip()
                manager.load_books_from_file(filename)
            case "7":
                print("Exiting program.")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()