import math


def solution(line):
    # '정수'인 교점들 구하기

    intersections = []

    for i in range(len(line) - 1):
        A = line[i][0]
        B = line[i][1]
        E = line[i][2]
        for j in range(i + 1, len(line)):
            C = line[j][0]
            D = line[j][1]
            F = line[j][2]

            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)

            if x == math.floor(x) and y == math.floor(y):
                intersections.append((int(x), int(y)))

    # test
    # print(intersections)

    # 정답 배열(사각형)의 최소 크기 정하기
    if intersections:
        x_min = intersections[0][0]
        x_max = intersections[0][0]
        y_min = intersections[0][1]
        y_max = intersections[0][1]
        for i in range(len(intersections)):
            if intersections[i][0] < x_min:
                x_min = intersections[i][0]
            if intersections[i][0] > x_max:
                x_max = intersections[i][0]
            if intersections[i][1] < y_min:
                y_min = intersections[i][1]
            if intersections[i][1] > y_max:
                y_max = intersections[i][1]

        # test
        # print(x_min, x_max, y_max, y_min)

        coordinate = ["." * (x_max - x_min + 1)] * (y_max - y_min + 1)
        # test
        # print(coordinate)

        # 교점 -> "*"
        for intersection in intersections:
            row = y_max - intersection[1]
            column = intersection[0] - x_min
            # test
            # print(row, column)

            coordinate[row] = coordinate[row][:column] + "*" + coordinate[row][column + 1:]
        # test
        # print(coordinate)

        return coordinate
    else:
        return [""]


line1 = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
line2 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
line3 = [[1, -1, 0], [2, -1, 0]]
line4 = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]

answer = solution(line1)
print(answer)
answer = solution(line2)
print(answer)
answer = solution(line3)
print(answer)
answer = solution(line4)
print(answer)
