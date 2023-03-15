def solution(board, moves):
    heights = [len(board) for i in range(len(board[0]))]    # heights 초기화 유의
    bucket = list()
    answer = 0

    # 각 줄마다의 '최고 높이' 기록 => heights
    for i in range(len(board)):
        for j in range(len(board[0])):
            if heights[j] == len(board) and board[i][j] != 0:
                heights[j] = i

    # 각 move의 최고 높이에 있는 인형에 대한 처리
    for i in range(len(moves)):
        move = moves[i]  # 가로 줄
        height = heights[move - 1]  # 해당 줄의 최고 높이

        if height < len(heights):
            selected_doll = board[height][move - 1]

            # board에서 제거
            board[height][move - 1] = 0

            # 해당 줄의 최고 높이 갱신
            heights[move - 1] += 1

            # bucket에 추가
            prior_bucket_top = bucket[-1] if len(bucket) != 0 else -1
            bucket.append(selected_doll)
            present_bucket_top = selected_doll
            # 기존 마지막 인형 & 현재 마지막 인형 비교
            # 만약 같으면 => bucket에서 제거 & answer + 2
            if prior_bucket_top == present_bucket_top:
                bucket.pop()
                bucket.pop()
                answer += 2

        # 디버그
        #print(i+1, "번째")
        #print(board)
        #print(bucket)
        #print(answer)

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
output = solution(board, moves)
print(output)

# 놓쳤던 테스트케이스
board_t1 =  [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [0, 2, 4, 4, 2], [0, 5, 1, 3, 1]]
moves_t1 = [1, 1]
output_t1 = solution(board_t1, moves_t1)
print(output_t1)
