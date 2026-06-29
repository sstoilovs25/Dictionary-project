import argparse
import io
from contextlib import redirect_stdout
from io import StringIO

from master_analyzer.statistics import generate_file_statistics, generate_multiple_file_statistics, format_statistics, count_word_frequencies, find_unknown_words, get_top_words
from master_analyzer.text_processing import load_text, extract_words
from master_analyzer.dictionary import load_dictionary
from master_analyzer.similarity import calculate_similarity


def show_dictionary_statistics(dictionary):

    result = []

    result.append("DICTIONARY")
    result.append(f"Lines: {dictionary['line_count']}")
    result.append(f"Words: {dictionary['word_count']}")
    result.append(f"Unique words: {dictionary['unique_words']}")

    return "\n".join(result)


def show_file_statistics(stats, work_files):
    result = []
    if len(work_files) == 1:

        print(format_statistics(stats))

    else:
        result.append("Total")
        print(format_statistics(stats["total"]))

        for file, file_stats in stats["files"].items():
            print(f"\n{file}")

            print(format_statistics(file_stats))


def show_unknown_words(stats, dictionary):


    unknown = find_unknown_words(stats["frequencies"], dictionary["unique_words"])

    for word, count in unknown.items():
        print(word, count)


def show_frequencies(stats, n):
    top = get_top_words(stats["frequencies"],n )

    for word, count in top:
        print(word, count)


def show_similarity(stats, work_files, n):
    freq1 = stats["files"][work_files[0]]["frequencies"]

    for file in work_files[1:]:
        freq2 = stats["files"][file]["frequencies"]

        similarity = calculate_similarity(
            freq1,
            freq2,
            n
        )

        print(file, ":", similarity, "%")


def main():
    parser = argparse.ArgumentParser(description="Master language Analyzer")
    parser.add_argument("--dictionary", required=True, help="Path to dictionary file")
    parser.add_argument("--works", required=True, help="Comma separated list of works")
    parser.add_argument("--dictionary-stats", action="store_true")
    parser.add_argument("--no-words", action="store_true")
    parser.add_argument("--frequencies", type=int, help="Number of most frequent words")
    parser.add_argument("--output", help="Output file")
    args = parser.parse_args()

    dictionary = load_dictionary(args.dictionary)
    work_files = args.works.split(",")

    buffer = io.StringIO()

    with redirect_stdout(buffer):

        if len(work_files) == 1:
            stats = generate_file_statistics(work_files[0])
            current_stats = stats

        else:
            stats = generate_multiple_file_statistics(work_files)
            current_stats = stats["files"][work_files[0]]

        if args.dictionary_stats:
            show_dictionary_statistics(dictionary)
            show_file_statistics(stats, work_files)

        if args.no_words:
            show_unknown_words(current_stats, dictionary)

        if args.frequencies:
            show_frequencies(current_stats, args.frequencies)

            if len(work_files) > 1:
                show_similarity(stats,work_files, args.frequencies)

    result = buffer.getvalue()

    if args.output:

        with open(args.output, "w", encoding="utf-8") as file:
            file.write(result)

    else:
        print(result)

if __name__ == "__main__":
    main()
