ans = ['factor', 'multiple', 'neither']

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        if a % b == 0:
            print(ans[1])
        else:
            print(ans[2])
    elif a < b:
        if b % a == 0:
            print(ans[0])
        else:
            print(ans[2])