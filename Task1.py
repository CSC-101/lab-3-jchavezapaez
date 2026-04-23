# Part 1
more = [x + 1 for x in [1,2,3,4]]                   # i1 -> x: 1, i2 -> x: 2, i3 -> x: 3, i4 -> x: 4
print()                                             # more: [2, 3, 4, 5]

# Part 2
def square(n:int) -> int:
    return n * n                                    # i1 -> n: 1, i2 -> n: 2, i3 -> n: 3, i4 -> n: 4
                                                    # i1 -> return: 1, i2 -> return: 4, i3 -> return: 9, i4 -> return: 16


squares = [square(x) for x in [1,2,3,4]]            # squares: [1, 4, 9, 16]
print()                                             # the value of squares is a list with elements corresponding to the return values in the same call order

# Part 3
def check(n:int) -> bool:
    return n > 2                                    # i1 -> n: 0, i2 -> n: 1, i3 -> n: 2, i4 -> n: 3, i5 -> n: 4
                                                    # i1 -> result: False, i2 -> result: False, i3 -> result: False, i4 -> result: True, i5 -> result: True


answer = [x for x in range(5) if check(x)]          # answer: [3, 4]
print()

# Part 4
def inc(m:int) -> int:
    return m + 1                                    # i4 -> m: 3, i5 -> m: 4
                                                    # i4 -> result: 4, i5 -> result: 5


def check(n:int) -> bool:
    return n > 2                                    # i1 -> n: 0, i2 -> n: 1, i3 -> n: 2, i4 -> n: 3, i5 -> n: 4
                                                    # i1 -> result: False, i2 -> result: False, i3 -> result: False, i4 -> result: True, i5 -> result: True


answer = [inc(x) for x in range(5) if check(x)]     # answer: [4, 5]
print()