import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 산술평균
print(round(sum(arr) / n))

# 중앙값
arr.sort()
print(arr[n//2])

# 최빈값
dic = dict()
for i in arr:
    if (i in dic):
        dic[i] += 1
    else:
        dic[i] = 1

dic_max = []
for i in dic:
    if (dic[i] == max(dic.values())):
        dic_max.append(i)

if (len(dic_max) > 1):
    print(dic_max[1])
else:
    print(dic_max[0])

# 범위
print(max(arr) - min(arr))