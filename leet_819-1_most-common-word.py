# ver.1 : list comprehension & Counter object
import collections
import re
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # 1) Data cleansing => regular expression
    words = [word for word in re.sub(r'\W', ' ', paragraph)
        .lower().split()
             if word not in banned]

    # 2) number of each word => Counter object
    counts = collections.Counter(words)

    # 3) pick "most common" words => Counter object's most_common() function
    return counts.most_common(1)[0][0]


paragraph_1 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned_1 = ["hit"]
paragraph_2 = "a."
banned_2 = []

result_1 = mostCommonWord(paragraph_1, banned_1)
print(result_1)

result_2 = mostCommonWord(paragraph_2, banned_2)
print(result_2)
