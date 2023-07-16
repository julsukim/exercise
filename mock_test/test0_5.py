T = int(input())

for i in range(1, T + 1):
    Case = input().split()
    int_Case = list(map(int, Case))
    odd = []
    for j in range(len(int_Case)):
        if int_Case[j] % 2 == 1:
            odd.append(int_Case[j])
    print('#' + str(i), sum(odd))