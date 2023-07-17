word = input().lower().replace(' ', '')

def palindrome(x):
    backward = x[::-1]

    if x == backward:
        return(True)
    else:
        return(False)
    
print(palindrome(word))