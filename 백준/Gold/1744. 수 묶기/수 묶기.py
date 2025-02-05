import sys
input = sys.stdin.readline

pos = []  # 양수
neg = []  # 음수
zero = 0  # 0의 개수
one = 0   # 1의 개수
ans = 0

# 숫자 분류
for _ in range(int(input())):
   num = int(input())
    
   if (num > 1):
       pos.append(num)
   elif (num == 1):
       one += 1
   elif (num == 0):
       zero += 1
   else:
       neg.append(num)

# 양수 처리 (내림차순)
pos.sort(reverse=True)

for i in range(0, len(pos)-1, 2):
   if (i+1 < len(pos)):
       ans += pos[i] * pos[i+1]
       
if (len(pos) % 2):
   ans += pos[-1]

# 음수 처리 (오름차순)
neg.sort()

for i in range(0, len(neg)-1, 2):
   if (i+1 < len(neg)):
       ans += neg[i] * neg[i+1]
       
if (len(neg) % 2):
   if zero == 0:
       ans += neg[-1]

print(ans+one)