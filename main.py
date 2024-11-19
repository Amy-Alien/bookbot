import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print("The number of words in the book:", count_words(file_contents))
    print(count_characters(file_contents))

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    dict = {}
    for i in string.ascii_lowercase:
        sum = 0
        for j in range(len(text)):
            if i == text[j]:
                sum += 1
        dict[i] = j
    
    return dict
                
if __name__ == "__main__":
    main()