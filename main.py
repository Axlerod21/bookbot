def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = list(get_num_letters(text).items())
    num_letters.sort()
    print(f"{num_words} words found in the document")

    for letter in num_letters:
        print(f"{letter[0]} was found {letter[1]} times")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            letters[letter.lower()] = letters.get(letter.lower(), 0) + 1
    
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()