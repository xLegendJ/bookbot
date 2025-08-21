def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def get_num_char(text):
    char_count = {}
    transform = text.lower()
    for i in transform:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def char(items):
    return items["num"]

def sort_char_count(sort_text):
    sorted = []
    for i in sort_text:
        if i.isalpha():
            sorted.append({"char": i, "num": sort_text[i]})
    sorted.sort(key=char, reverse=True)
    return sorted
