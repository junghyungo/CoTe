n, m = map(int,input().split())
nums = list(map(int,input().split()))
max=0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = nums[i]+nums[j]+nums[k]
            if(sum<=m and sum>max):
                max=sum
                
print(max)