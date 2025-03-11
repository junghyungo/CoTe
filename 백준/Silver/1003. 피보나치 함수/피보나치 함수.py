import sys
input = sys.stdin.readline

def fibonacci_counts(n):
    a, b = 1, 0  # f(0) 호출 횟수, f(1) 호출 횟수
    c, d = 0, 1  # f(0) 호출 횟수, f(1) 호출 횟수 (n=1일 때)
    
    for _ in range(n):
        a, b = b, a + b  # 0 호출 횟수 갱신
        c, d = d, c + d  # 1 호출 횟수 갱신
    
    return a, c

for _ in range(int(input())):
    print(*fibonacci_counts(int(input())))