def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    book_text = get_book_text(file_path)
    words = book_text.split()
    num_words = len(words)
    return num_words
    #print(f"{num_words} words found in the document")

def character_count(text: str) -> dict:
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_counts(char_counts):
    # Filter out non-alphabetical characters
    filtered_counts = [{ "char": char, "num": count } for char, count in char_counts.items() if char.isalpha()]
    
    # Sort the list by count in descending order
    filtered_counts.sort(key=lambda x: x["num"], reverse=True)
    
    return filtered_counts
