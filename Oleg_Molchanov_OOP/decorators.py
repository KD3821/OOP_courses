from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

# @timeit
def one(n):
    l = []
    for x in range(n):
        if x % 2 == 0:
            l.append(x)
    return l

# @timeit
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

a = timeit(one)

# a = one
# b = a(10)
# print(b)
