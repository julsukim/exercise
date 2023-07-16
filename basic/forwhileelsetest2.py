countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    if input() == '중단':
        break
else:
    print('발사!')