from functools import total_ordering


total = 3000
distance = 1000
load = 1000
loss = 0
start = total

for i in range(distance):
    while start > 0:
        start = start - load
        if start == 1:
            loss = loss - 1
        loss = loss + 2
    loss = loss - 1
    start = total - loss
    if start == 0:
        break
print(start)
