def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters = count_letter(text)
    # print(text)
    print(f"{num_words} words found in the document")
    print(f"{num_letters} letters found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_str):
    return len(book_str.split())

def count_letter(book_str):
    normalized_str = book_str.lower()
    letters = {}

    for str in normalized_str:
        if str in letters:
            letters[str] += 1
            continue
        letters[str] = 1

    return letters

main()