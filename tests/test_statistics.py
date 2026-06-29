from master_analyzer.dictionary import load_dictionary
from master_analyzer.text_processing import extract_words, load_text
from master_analyzer.statistics import (count_word_frequencies, find_unknown_words, generate_text_statistics,
                                        generate_file_statistics, generate_multiple_file_statistics)
dictionary = load_dictionary("data/dictionary/odm.txt")

text = load_text("data/works/Gutenberg-sam.txt")
words = extract_words(text)
frequencies = count_word_frequencies(words)
unknown_words = find_unknown_words(frequencies, dictionary["unique_words"])
print("Unknow words:", len(unknown_words))
# for word, count in list(unknown_words.items())[:20]:
#     print(word, count)
# sorted_unknown = sorted(
#     unknown_words.items(),
#     key=lambda item: (-item[1], item[0])
# )
#
# for word, count in sorted_unknown[:30]:
#     print(word, count)

text = "który cała jedna"

words = extract_words(text)

print(words)

stats2 = generate_file_statistics("data/works/Gutenberg-sam.txt")
stats3 = generate_file_statistics("data/works/Gutenberg-oryginalny.txt")
print ("Words file1",stats2["word_count"])
print (stats3["word_count"])

print("Line count1",stats2["line_count"])
print(stats3["line_count"])


statss = generate_multiple_file_statistics(["data/works/Gutenberg-sam.txt",
                                           "data/works/Gutenberg-oryginalny.txt"])
print(statss["total"]["file_count"])
print(statss["total"]["word_count"])




from collections import Counter
from master_analyzer.similarity import calculate_similarity
f1 = Counter({
    "cat": 10,
    "dog": 5,
    "bird": 2
})

f2 = Counter({
    "cat": 8,
    "dog": 5,
    "fish": 3
})

print("similarity is:",calculate_similarity(f1, f2))

from master_analyzer.statistics import count_word_frequencies

freq = count_word_frequencies(
    ["cat", "dog", "cat"]
)

print(freq)