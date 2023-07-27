파이썬을 이용한 자료구조 및 알고리즘 공부 레포지토리 입니다.

1. Valid Palindrome
  - https://leetcode.com/problems/valid-palindrome/
  - 풀이 버전
    - ⓐ list()
    - ⓑ Deque
    - ⓒ slicing(슬라이싱) & 정규표현식

2. Reverse String
  - https://leetcode.com/problems/reverse-string/
  - 풀이 버전
    - ⓐ Swap with Two-Pointer (전통적 방식)
    - ⓑ reverse() (파이썬다운 방식)

3. Reorder Log Files
  - https://leetcode.com/problems/reorder-data-in-log-files/
  - 풀이 버전
    - ⓐ lambda expression & + operator

4. Most Common Word
- https://leetcode.com/problems/most-common-word/
- 풀이 버전
  - ⓐ list comprehension & Counter object

5. [silver-4] ATM
- https://www.acmicpc.net/problem/11399
- 그리디, 정렬
- 풀이 결과
    - first trial : 너무 직관적으로 풀이함
    - second trial : 좀 더 수학적으로 접근

6. [level-1] 크레인 인형뽑기 게임
- https://school.programmers.co.kr/learn/courses/30/lessons/64061
- 스택
- 풀이 결과
    - first trial : 주어진 테스트케이스와 다른 비공개 테스트케이스 하나는 통과했지만, 나머지 테스트케이스들에 대해서는 실패함.
    - second trial : 애초에 board의 (세로)줄에 인형이 들어있지 않은 케이스를 고려해주니까 전체 테스트케이스 통과함.
        - 놓쳤던 테스트케이스 출처 : https://algoroot.tistory.com/75

7. [silver-5] 그룹 단어의 개수
- https://www.acmicpc.net/problem/1316
- 문자열, 구현
- 풀이 결과
    - first trial : 첫 시도만에 통과. collections.Counter()를 사용해서 풀어봄. 디버그를 코드 옆에 실시간으로 주석 다는 식으로 하니까 더 잘 됐음.
        - 참고 출처
            - '입력' : https://happyeuni.tistory.com/18
            - 'collections' : https://daco2020.tistory.com/m/229

8. [silver-1] 1로 만들기 ver.2
- https://www.acmicpc.net/problem/12852
- Dynamic Programming
- 풀이 결과
    - first trial : '중복된' 계산이 발생한다는 점을 이용해서 dynamic programming의 memoization 기법으로 값을 재활용해야겠다는 생각을 했다.
        - 참고 출처
            - 'dynamic programming' : https://hongjw1938.tistory.com/47

9. [level-2] 교점에 별 만들기
- https://school.programmers.co.kr/tryouts/72046/challenges
- 배열 > 2차원 배열
- 풀이 결과
  - first trial : line2에서 'ZeroDivisionError' 오류 발생
  - second trial : if 문 추가 => ZeroDivisionError 오류 해결
  - 