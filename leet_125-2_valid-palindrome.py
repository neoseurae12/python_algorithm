# ver.2 : Deque

import collections


def isPalindrome(s: str) -> bool:
  # declare as "Deque"
  strs = collections.deque()

  # make deque have only english(lower case) & number
  for c in s:
    if c.isalnum():
      strs.append(c.lower())

  # check if it's palindrome
  while len(strs) > 1:
    if strs.pop() != strs.popleft():
      return False
  
  return True

input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"
print(isPalindrome(input1))
print(isPalindrome(input2))

'''
True
False
'''