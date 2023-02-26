# ver.1 : Swap with Two-Pointer

from typing import List

def reverseString(s: List[str]) -> None:
  # index -- left & right
  left, right = 0, len(s)-1

  # swap : s[left] <-> s[right]
  while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

input1 = ["h", "e", "l", "l", "o", ]
input2 = ["H", "a", "n", "n", "a", "h"]
reverseString(input1)
print(input1)
reverseString(input2)
print(input2)