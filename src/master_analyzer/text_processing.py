def load_text(path:str):
    with open(path, encoding='utf-8') as file:
         text = file.read()

    return text

def count_lines(path:str):
    with open(path, encoding='utf-8') as file:
        return sum(1 for _ in file)

import re
def extract_words(text:str):

    return re.findall(r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+", text)
    # text = text.lower()
    # words[]
    # for word in text:
    #     word = word.strip(".,!?;;()[]{}\"'")
    #     if word:
    #         words.append(word)


if __name__ == '__main__':
    text1 = load_text("data/works/Gutenberg-sam.txt")
    words = extract_words(text1)
    print(text1)
    print("words", len(words))
    print("lines", count_lines("data/works/Gutenberg-sam.txt"))
    print("unique words", len(set(words)))
    print (words[:20])