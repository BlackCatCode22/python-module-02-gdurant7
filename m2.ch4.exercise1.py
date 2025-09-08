import random

for i in range(10):
    x = random.random()
    print(x)

for i in range (5):
    x = random.randint(5, 10)
    print(x)

for i in range (5): #book needs more detail on random.choice(t)
    t = [1, 2, 3]
    random.choice(t)
    print(t)