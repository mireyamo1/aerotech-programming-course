def sum_up(*args):
    sum=0
    for i in args:
        sum = sum + i
    return 2*sum

print(sum_up(1, 1, 3))

