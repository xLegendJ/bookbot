from stats import get_num_words
from stats import get_num_char
from stats import char
from stats import sort_char_count
import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_char = get_num_char(book_text)
    print("--------- Character Count -------")
    sorted_list  = sort_char_count(num_char)
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
