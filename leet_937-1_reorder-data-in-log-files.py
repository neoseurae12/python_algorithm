# ver.1 : lambda & + operator

# ① split the logs into two categories : letters & digits => isdigit()
# ② 'letters' logs => sort() -- key : 1) letter log, 2) identifier
# ③ 'digits' logs => append()
# ④ put the two 'letters' logs & 'digits' logs together => + operator

from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
  # ① split the logs into two categories : letters & digits => isdigit()
  letters = list()
  digits = list()

  for log in logs:
    if log.split()[1].isdigit():
      # ③ 'digits' logs => append()
      digits.append(log)
    else:
      letters.append(log)

  #print(digits)
  #print(letters)

  # ② 'letters' logs => sort() -- key : 1) letter log, 2) identifier
  letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
  #print(letters)

  # ④ put the two 'letters' logs & 'digits' logs together => + operator
  return letters + digits


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))