from collections import Counter
from master_analyzer.text_processing import extract_words,load_text, count_lines


def count_word_frequencies(words):
    # freq = {}
    # for word in words:
    #     if word in freq:
    #         freq[word] += 1
    #     else :
    #         freq[word] = 1
   return Counter(words)
if __name__ == "__main__":

    sample = [
        "cat",
        "dog",
        "cat",
        "bird",
        "cat"
    ]

    frequencies = count_word_frequencies(sample)
    print(frequencies)




def find_unknown_words(frequencies, dictionary_words):
    unknown_words = {}
    for word, count in frequencies.items():
        if word.lower() not in dictionary_words:
            unknown_words[word] = count

    return unknown_words

def get_top_words(frequencies, n=10):
    sorted_words = sorted(frequencies.items(),key=lambda item: (-item[1], item[0]))

    if len(sorted_words) <= n:
        return sorted_words

    threshold = sorted_words[n - 1][1]
    result = []
    for word, count in sorted_words:

        if count >= threshold:
            result.append((word, count))

    return result

if __name__ == "__main__":
   sample2 = [
        "cat",
        "dog",
        "cat",
        "bird",
        "cat",
        "bird",
        "bird",
        "bird"
    ]

# print(get_top_words(sample2, 2))

def count_letters(words):
    letters = Counter()
    for word in words:
        for letter in word:
            letters[letter] += 1

    letters = sorted(letters.items(), key=lambda item: (-item[1], item[0]))
    return letters

if __name__ == "__main__":
    sample2 =  [
    "cat",
    "dog"
    "acog"
]
    print("count letters:",count_letters(sample2))

def generate_text_statistics(words):
    frequencies = count_word_frequencies(words)
    return {
        "word_count": len(words), "unique_word_count": len(frequencies), "frequencies": frequencies,
        "top_words":get_top_words(frequencies), "letter_counts": count_letters(words)
    }
if __name__ == "__main__":
   stats1 = generate_text_statistics(["cat", "dog", "cat"])
   print(stats1)


def generate_file_statistics(path:str):
    text = load_text(path)
    words = extract_words(text)
    stats = generate_text_statistics(words)
    stats["line_count"] = count_lines(path)
    return stats

if __name__ == "__main__":
    stats = generate_file_statistics("data/works/Gutenberg-sam.txt")
    print(stats["line_count"])
    print(stats["unique_word_count"])
    print(stats["word_count"])

def generate_multiple_file_statistics(paths):
    file_results = {}
    all_words = []
    total_lines = 0
    for path in paths:
        per_each_file = generate_file_statistics(path)
        file_results[path] = per_each_file
        text = load_text(path)
        words = extract_words(text)
        all_words.extend(words)
        total_lines += per_each_file["line_count"]
    total_stats = generate_text_statistics(all_words)
    total_stats["line_count"] = total_lines
    total_stats["file_count"] = len(paths)
    return {
        "files":file_results ,"total":total_stats
    }
def format_statistics(stats):

    output = []

    output.append(f"Lines: {stats['line_count']}")
    output.append(f"Words: {stats['word_count']}")
    output.append(f"Unique words: {stats['unique_word_count']}")

    output.append("\nTop words:")

    for word, count in stats["top_words"]:
        output.append(f"{word}: {count}")

    output.append("\nLetter frequencies:")

    for letter, count in stats["letter_counts"]:
        output.append(f"{letter}: {count}")

    return "\n".join(output)



