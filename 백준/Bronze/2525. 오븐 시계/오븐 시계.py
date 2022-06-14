h,m = map(int, input().split())
c = int(input())

print( (h+((m+c)//60))%24, (m+c)%60 )