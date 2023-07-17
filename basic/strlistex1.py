str_num = list(input())
int_num = []

def sumOfDigits(x):
    for i in range(0, len(x)):
        int_num.append(int(x[i]))
        
    return sum(int_num)

print(sumOfDigits(str_num))