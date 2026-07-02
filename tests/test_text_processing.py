from master_analyzer.text_processing import extract_words
def test_extract_words():
    words = extract_words("Cat dog cat")
    assert words == ["Cat", "dog", "cat"]