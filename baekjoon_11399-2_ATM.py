# second trial

# 입력 처리
N = int(input())
P = list(map(int, input().split()))

answer = 0

# 정렬
P.sort()

# 합
for i in range(N):
    answer += P[i]*(N-i)

print(answer)
