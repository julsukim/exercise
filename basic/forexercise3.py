L = input().split()
min = int(L[0])
max = int(L[1])

temp = int(input())

while temp != -999:
    if min <= temp <= max:
        print('Nothing to report')
        temp = int(input())
    else:
        print('Alert!')
        break