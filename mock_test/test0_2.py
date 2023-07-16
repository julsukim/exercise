N = str(input())

if len(N) == 4:
    print(int(N[0]) + int(N[1]) + int(N[2]) + int(N[3]))
elif len(N) == 3:
    print(int(N[0]) + int(N[1]) + int(N[2]))
elif len(N) == 2:
    print(int(N[0]) + int(N[1]))
elif len(N) == 1:
    print(int(N[0]))