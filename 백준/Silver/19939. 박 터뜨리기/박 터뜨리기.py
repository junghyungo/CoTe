n, k = map(int, input().split())

# 공의 최소 필요 개수 (= k + (k - 1) + (k - 2) + ... + 1)
sum_of_sequence = (k * (k+1)) // 2

# n이 최소 필요 개수 보다 작을때
if (n < sum_of_sequence):
    print(-1)

# k로 나누어 떨어지는 경우
# 즉, k개의 바구니에 균등 분배 가능한 경우
elif ((n - sum_of_sequence) % k == 0):
    print(k-1)

# 균등 분배가 불가능한 경우
else:
    print(k)