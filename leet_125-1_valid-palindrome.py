# ver.1 : list()

def isPalindrome(s: str) -> bool:
  # make a 'list'
  result = list()
  for c in s:
    if c.isalnum():
      result.append(c.lower())

  # pop first & last
  while len(result) > 1:
    # compare (same/different)
    if result.pop(0) != result.pop():
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