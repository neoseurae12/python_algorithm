# ver.2 : reverse()

from typing import List

def reverseString(s: List[str]) -> None:
    s.reverse()

input1 = ["h", "e", "l", "l", "o", ]
input2 = ["H", "a", "n", "n", "a", "h"]
reverseString(input1)
print(input1)
reverseString(input2)
print(input2)