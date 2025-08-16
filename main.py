import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
     
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    num_words = get_num_words(get_book_text(filepath))
    num_chars = get_num_chars(get_book_text(filepath))
    chars_sorted = sort_chars(num_chars)
    header_text = f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------"
    print(header_text)

    lines = []
    for item in chars_sorted:
        if item["char"].isalpha():
            lines.append(f"{item["char"]}: {item["num"]}")

    lines.append("============= END ===============")
    print('\n'.join(lines))

main()