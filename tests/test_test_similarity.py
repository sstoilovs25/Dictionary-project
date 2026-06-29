from master_analyzer.similarity import calculate_similarity

freq1 = {
    "cat": 3,
    "dog": 2
}

freq2 = {
    "cat": 3,
    "dog": 1
}

print(
    calculate_similarity(
        freq1,
        freq2,
        2
    )
)
