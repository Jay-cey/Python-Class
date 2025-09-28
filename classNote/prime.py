num =  int(input(">>>"))

def isPrime():
    if num <= 1:
        return False
    for i in range(2, (num ** 0.5) + 1):
        if num % i == 0:
            return False
    return f"{num} is a "