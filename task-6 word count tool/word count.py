from collections import Counter
import string
filename = "sample.txt"

try:
   
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    
    lines = text.splitlines()
    line_count = len(lines)


    character_count = len(text)

    
    text_lower = text.lower()

    
    text_clean = text_lower.translate(
        str.maketrans("", "", string.punctuation)
    )

  
    words = text_clean.split()

   
    word_count = len(words)

    word_frequency = Counter(words)

    
    print("=" * 40)
    print("          WORD COUNT TOOL")
    print("=" * 40)

    print(f"File Name       : {filename}")
    print(f"Number of Lines : {line_count}")
    print(f"Number of Words : {word_count}")
    print(f"Characters      : {character_count}")

    print("\nMost Frequently Used Words:")
    print("-" * 40)

    for word, count in word_frequency.most_common(10):
        print(f"{word:<20} : {count}")

    print("=" * 40)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

except Exception as e:
    print("An error occurred:", e)