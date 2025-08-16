def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars = {}
    for ch in text:
        ch = ch.lower()
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1

    return chars

def sort_on(ls):
    return ls["num"]

def sort_chars(dictionary):
    ls = []

    for key, value in dictionary.items():
        ls.append({"char": key, "num": value})

    ls.sort(reverse=True, key=sort_on)
    return ls