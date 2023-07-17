num = int(input())

def korean_number(x):
    kor_numlist = {0 : '영', 1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', 6 : '육', 7 : '칠', 8 : '팔', 9 : '구'}
    return kor_numlist[x]

print(korean_number(num))