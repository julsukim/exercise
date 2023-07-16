def quiz():
    ans = input('1 + 2 = ')
    return 1 + 2 == int(ans)
if quiz() == True:
    print('yes')
else:
    print('DDang')