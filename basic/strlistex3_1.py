num = list(input())

def sumOfDigits(x):
    sum_num = list(map(int, x))
    return sum(sum_num)

print(sumOfDigits(num))