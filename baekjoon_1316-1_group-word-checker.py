import collections


def group_word_checker(n: int, words: list) -> int:
    answer = 0

    for word in words:
        word_dict = collections.Counter(word)
        answer += 1

        for i in range(len(word) - 1):
            prev_alphabet = word[i]  # h a p p
            now_alphabet = word[i + 1]  # a p p y

            word_dict[prev_alphabet] -= 1  # {h:0, a:0, p: 0, y:1}

            if prev_alphabet != now_alphabet:
                if word_dict[prev_alphabet] != 0:
                    answer -= 1
                    break

    return answer


# 입력
N = int(input())
P = [input() for _ in range(N)]

# 출력
result = group_word_checker(N, P)
print(result)
