import string


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count: # Если буква в словаре есть мы прибавлем 1 к счетчику
                char_count[char] += 1
            else: # Если буквы в словаре нет мы инициализируем счетчик для этого символа
                char_count[char] = 1
    
    return char_count
            
def generate_report(file_path):
    
    with open(file_path) as file:
        text = file.read()
        
    word_count = count_words(text)
    char_count = count_characters(text)
    
    # Print report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")

    # Sort chars
    sorted_char = sorted(char_count.items(), key= lambda item: item[1], reverse=True)
    # Print sorted chars
    for char, count in sorted_char:
        print(f"The '{char}' character was found {count} items")
    
    print("--- End report ---")
        

def main():
    file_path = "books/frankenstein.txt"

    generate_report(file_path)
    

if __name__ == "__main__":
    main()