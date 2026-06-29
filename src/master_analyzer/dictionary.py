
def load_dictionary(path:str):

    line_count = 0
    all_words = set()
    word_count =0
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            line_count += 1
            if not line:
                continue

            forms = [word.strip().lower() for word in line.split(",")]
            # entries.append(forms)

            for word in forms:
                word_count += 1
                all_words.add(word)

    return{"line_count": line_count,"word_count":word_count, "unique_words": all_words}


if __name__  == "__main__":
    dictionary= load_dictionary("data/dictionary/odm.txt")
    print("Lines:", dictionary["line_count"])
    print("Unique words:", len(dictionary["unique_words"]))
    print("Word_count:",dictionary["word_count"])

