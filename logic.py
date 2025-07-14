def wordcount(text, input):
    lowercase_text = text.lower()
    word = input.lower()
    count = lowercase_text.count(word)
    return f"The word '{word}' appears {count} times."
    