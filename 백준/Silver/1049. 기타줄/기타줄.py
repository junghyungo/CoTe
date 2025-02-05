import sys
input = sys.stdin.readline

Cheapest_Package, Cheapest_Each = 1001, 1001

n, m = map(int, input().split())

# m개 브랜드들의 가격중 제일 싼거 찾기
for i in range(m):
    Package, Each = map(int, input().split())
    Cheapest_Package = min(Cheapest_Package, Package)
    Cheapest_Each = min(Cheapest_Each, Each)

# 패키지로만 (6이하로 남은 줄이 있어도 하나 더 사야함)
ans = (n//6 + (1 if n%6 else 0)) * Cheapest_Package

# 낱개로만
ans = min(ans, n * Cheapest_Each)

# 섞어서
ans = min(ans, (n//6)*Cheapest_Package + (n%6)*Cheapest_Each)

print(ans)