def main():
    filename = 'books/frankenstein.txt'
    text = read_file(filename)
    num_words = count_words(text)
    char_count = count_letters(text)
    sorted_list = char_sorted_list(char_count)

    #print(sorted_list)

    print(f"--- Begin report of {filename} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print()
    print("--- End report ---")

    
def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split() 
    return len(words)

def count_letters(text):
    char_count_dict = {}
    characters = text.lower()

    for character in characters:
        if character in char_count_dict:
            char_count_dict[character] += 1
        else:
            char_count_dict[character] = 1
        
    return char_count_dict
def sort_on(d):
    return d["num"]

def char_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()