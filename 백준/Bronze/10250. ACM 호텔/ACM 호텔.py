for i in range(int(input())):
    h,w,n = map(int, input().split())
    print(f'{h*100+n//h}' if n%h==0 else f'{n%h*100+(n//h+1)}')