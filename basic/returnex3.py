p = float(input())
r = float(input())
t = float(eval(input()))

def simple_interest(x, y, z):
    return x * y * z

def simple_interest_amount(x, y, z):
    return x * (1 + y * z)

print(simple_interest(p, r, t))
print(simple_interest_amount(p, r, t))