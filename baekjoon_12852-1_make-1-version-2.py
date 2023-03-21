def solution(N: int):
    # dp : [거친 n, n의 연산횟수]
    dp = [[0, 0]] * (N + 1)

    # dp 업데이트
    for i in range(2, N + 1):
        three = [i - 1, dp[i - 1][1] + 1]

        if i % 3 == 0 and i % 2 == 0:  # 6의 배수
            # 6의 배수
            one = [i // 3, dp[i // 3][1] + 1]
            two = [i // 2, dp[i // 2][1] + 1]
            if one[1] <= three[1]:
                dp[i] = one
                if two[1] <= one[1]:
                    dp[i] = two
            else:
                dp[i] = three
        elif i % 3 == 0:  # 3의 배수
            one = [i // 3, dp[i // 3][1] + 1]
            if one[1] <= three[1]:
                dp[i] = one
            else:
                dp[i] = three
        elif i % 2 == 0:  # 2의 배수
            two = [i // 2, dp[i // 2][1] + 1]
            if two[1] <= three[1]:
                dp[i] = two
            else:
                dp[i] = three
        else:  # 2의 배수도, 3의 배수도 아닌 수
            dp[i] = three

    # 출력
    print(dp[N][1])
    tracking = N
    while tracking > 0:
        print(tracking, end=" ")
        tracking = dp[tracking][0]


N = int(input())
solution(N)
