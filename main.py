
def print_report():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"{len(file_contents.split())} words found in the document")
        
        characters_count = {}
        for character in file_contents.lower():
            characters_count[character] = characters_count.get(character, 0) + 1
        for character, count in characters_count.items():
            if character.isalpha():
                print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    print_report()