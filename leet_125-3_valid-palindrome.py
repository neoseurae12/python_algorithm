# ver.3 : slicing(슬라이싱) & 정규표현식

import re


def isPalindrome(s: str) -> bool:
  # -> lower case
  s = s.lower()

  # subtract NOT 'english OR number' with 정규표현식
  s = re.sub('[^a-z0-9]', '', s)

  # chech if it's palindrome with "slicing(슬라이싱)"
  return s == s[::-1]

input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"
print(isPalindrome(input1))
print(isPalindrome(input2))

'''
True
False
'''