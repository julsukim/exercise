N = int(input())
score = input().split()
order = N // 2

int_score = list(map(int, score))

int_score.sort()

print(int_score[order])