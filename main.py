def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letters_dict = count_letter(text)
    letters_lst = [letter for letter in letters_dict if letter.isalpha()]
    letters_lst.sort()
    print(letters_lst)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")

    for letter in letters_lst:
        print(f"The '{letter}' character was found {letters_dict[letter]} times")

    print("--- End report ---")

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