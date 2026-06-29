# import pandas as pd
# import Mathplotlib.piplot as mpl
from master_analyzer.statistics import get_top_words
def calculate_similarity(freq1,freq2, n):
    top1 = dict(get_top_words(freq1, n))
    top2 = dict(get_top_words(freq2, n))
    all_words = set(top1.keys()) | set(top2.keys())
    similarity = 0
    for word in all_words:
        counter1 = top1.get(word,0)
        counter2 = top2.get(word,0)
        if max(counter1,counter2)!=0:
            similarity += min(counter1, counter2) / max(counter1, counter2)

    similarity2 = (similarity/ len(all_words)) * 100
    return round(similarity2,2)



