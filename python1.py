# 리스트 컴프리헨션
list1 = [n*2 for n in range(1, 10+1) if n%2==1]
print(list1)
'''
출력결과
[2, 6, 10, 14, 18]
'''

# 제네레이터
def generator():
    yield 1
    yield 'string'
    yield True
g = generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
'''
출력결과
<generator object generator at 0x0000022D2A888B40>
1
string
True
'''