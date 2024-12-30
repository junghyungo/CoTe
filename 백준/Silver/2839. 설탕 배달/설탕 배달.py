n = int(input())
ans = 0

while True:
    if n < 0:
        ans = -1
        break
    else:
        if (n % 5) != 0:
            n -= 3
            ans += 1
        else:
            ans += n // 5
            break

print(ans)