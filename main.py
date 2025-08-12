import sys
from stats import get_num_words, get_num_characters, sorted_char_counts
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
         return f.read() 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    total_words = get_num_words(book_text)
    char_counts = get_num_characters(book_text)
    sorted_chars = sorted_char_counts(char_counts)

# sorting print:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()