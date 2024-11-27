import algorithm as al
import time
from random import randint
t = 0
for j in range(5):
    a = [randint(1, 100000) for i in range(100000)]
    Start = time.time()
    a = al.bubble_sort(a)
    Finish = time.time()
    t += (Finish - Start) * 1000
    print('1')
print(t/5)