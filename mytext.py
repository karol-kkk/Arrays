# MyText.py module

def count_words(text):
    words = text.split()
    return len(words)

def sort_by_length(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def sort_alphabetically(text):
    words = text.split()
    return sorted(words)
