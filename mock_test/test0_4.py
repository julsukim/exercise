T = int(input())

for i in range(1, T + 1):
    Case = input().split()
    int_Case = list(map(int, Case))
    int_Case.sort()
    print('#' + str(i), int_Case[-1])