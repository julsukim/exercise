num = int(input())

def korean_age(x):
    from datetime import datetime
    today = datetime.today()
    return today.year - x + 1

print(korean_age(num))