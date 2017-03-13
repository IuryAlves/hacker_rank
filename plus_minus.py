#!/bin/python3


n = int(input().strip())
numbers = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive, negative, zero = 0, 0, 0

for number in numbers:
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1
    if number == 0:
        zero += 1

print("%8.6f" % (positive / n))
print("%8.6f" % (negative / n))
print("%8.6f" % (zero / n))
