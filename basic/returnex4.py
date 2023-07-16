p = float(input())
r = float(input())
t = float(input())
n = float(eval(input()))

def compound_interest_amount(p, r, t, n):
    return p * (1 + r / n) ** (n * t)

print(compound_interest_amount(p, r, t, n))