import sys
from stats import character_count, get_book_text, get_num_words, sort_char_counts

def main():
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Get the file path from command line argument
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)

    # Get word count
    num_words = get_num_words(file_path)

    # Get character counts
    char_counts = character_count(book_text)

    # Get sorted character counts
    sorted_char_counts = sort_char_counts(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Print each character's count from the sorted list
    for char_count in sorted_char_counts:
        print(f"{char_count['char']}: {char_count['num']}")

    print("============= END ===============")

main()
