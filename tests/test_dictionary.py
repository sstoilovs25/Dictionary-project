from master_analyzer.dictionary import load_dictionary
def test_load_dictionary():
    dictionary = load_dictionary("data/dictionary/odm.txt")

    print(dictionary["line_count"] > 0)
    print(dictionary["word_count"] > 0)
    print(len(dictionary["unique_words"]) > 0)