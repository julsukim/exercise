number = int(input())

def sumOfDigits(num):
    sum = 0
    for c in list(str(num)):
        sum += int(c)

    return sum

print(sumOfDigits(number))