class Book:
    def __init__(self, book_path) -> None:
        self.__book_path = book_path
        self.__text = None

    def __get_text(self):
        if not self.__text:
            with open(self.__book_path) as f:
                return f.read()
        else:
            return self.__text

    def get_text(self):
        return self.__get_text()
        
    def get_book_path(self):
        return self.__book_path
        
    def get_word_count(self):
        words =  self.__get_text().split()
        return len(words)

    def get_chars_count(self):
        chars_dict = {}
        for char in self.__get_text().lower():
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
        return chars_dict
    
def main():
    book_path = "books/frankenstein.txt"
    book = Book(book_path)
    print(f"{book.get_book_path()} contains {len(book.get_text())} characters")
    print(f"{book.get_book_path()} contains {book.get_word_count()} words")
    chars_dict = book.get_chars_count()
    print(f"{book.get_book_path()} contains {len(book.get_chars_count())} unique characters")
    print(chars_dict)
        
main()