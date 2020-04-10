def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

it = primes()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

L = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(L)

def test01(n):
    return n
a = test01;
print(a(3))

L = list(filter(lambda n:n%2==1, range(1, 20)))
print(L)