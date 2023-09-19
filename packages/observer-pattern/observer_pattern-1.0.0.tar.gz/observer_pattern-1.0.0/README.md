# observer-pattern
Simple Observer Pattern Implementation

```python
from observer_pattern import Observable

counter = 0

def plus_n(n):
    global counter
    counter += n

def plus_2n(n):
    global counter
    counter += 2*n

def plus_3n(n):
    global counter
    counter += 3*n

observable = Observable()
observable.subscribe(plus_n)
observable.subscribe(plus_2n)
observable.subscribe(plus_3n)
observable.notify(2)
observable.unsubscribe(plus_3n)
observable.notify(5)

print(counter) # 27
print(len(observable)) # 2
```

You can pass any number of `args` and `kwargs`

```python
def print_product(a, b):
    print(a * b)

observable = Observable()
observable.subscribe(print_product)
observable.notify(3, b=5) # 15
print(print_product in observable) # True
```
