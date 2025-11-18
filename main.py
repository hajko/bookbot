import sys

from stats import get_char_counts, get_num_words, sort_char_dict


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    book_text = get_book_text(book)

    num_words = get_num_words(book_text)
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------""")
    print(f"Found {num_words} total words")

    char_dict = get_char_counts(book_text)
    sorted_chardict_list = sort_char_dict(char_dict)
    for item in sorted_chardict_list:
        if item.get("char").isalpha():
            print(f"{item.get('char')}: {item.get('num')}")

    print("============= END ===============")


main()
