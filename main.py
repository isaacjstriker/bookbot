def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num = get_char_num(text)
    print(f"{num_words} words found in the document")
    print(char_num)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_num(text):
    frequency = {}
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
