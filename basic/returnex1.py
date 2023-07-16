num = int(input())

def korean_number(x):
    if x == 1:
        return '일'
    elif x == 2:
        return '이'
    elif x == 3:
        return '삼'
    elif x == 4:
        return '사'
    elif x == 5:
        return '오'

print(korean_number(num))