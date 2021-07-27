import time

def dectime(fn):
    def tt(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = round(time.time() - start, 5)
        print(f"время выполнения: {end} сек")
    return tt

@dectime
def func2(N):
    l2 = [i for i in range(N+1) if i % 2 == 0 ]
    print(l2)

@dectime
def func1(N):
    l1 = []
    a = 0
    while a <= N:
        l1.append(a)
        a = a+2
    print(l1)



N = 10000
func1(N)
func2(N)

