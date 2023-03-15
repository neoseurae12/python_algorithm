# first trial

import sys


def atm(n: int, plist: list) -> int :
    answer = 0

    # 리스트 오름차순 정렬
    plist.sort()

    # 합 리스트
    sum_list = list()
    for i in range(n):
        sums = 0
        for j in range(i+1):
            sums += plist[j]
        sum_list.append(sums)

    # 최종 합
    for i in range(len(sum_list)):
        answer += sum_list[i]

    return answer


N = int(input())
P = list(map(int, input().split()))

result = atm(N, P)
print(result)
