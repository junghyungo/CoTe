a = 0
b = 1
ans = 0
for i in range(int(input())):
    a = b
    b = ans
    ans = a+b
print(ans)