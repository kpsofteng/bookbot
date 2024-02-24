def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_word_count(text):
    words =  text.split()
    return len(words)

def get_chars_count(text):
    s = {}
    for char in text.lower():
        if char in s:
            s[char] += 1
        else:
            s[char] = 1
    return s
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(f"{book_path} contains {len(book_text)} characters")
    print(f"{book_path} contains {get_word_count(book_text)} words")
    chars_dict = get_chars_count(book_text)
    print(f"{book_path} contains {len(get_chars_count(book_text))} unique characters")
    print(chars_dict)
        
main()