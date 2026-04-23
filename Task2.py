# Part 1
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num                         # i1 -> num: 4 & total: 4, i2 -> num: 9 & total: 13, i3 -> num: 2 & total: 15, i4 -> num: 1 & total: 16
    return total

result = tally([4, 9, 2, 1])

# Part 2
def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])                  # i1 -> idx: 0 & new_list: [4], i2 -> idx: 1 & new_list: [4, 9], i3 -> idx: 2 & new_list: [4, 9, 2], i4 -> idx: 3 & new_list: [4, 9, 2, 1]
    return new_list                                 # This loop iterates over indices to obtain values, while the loop above iterates over values directly

result = copy([4, 9, 2, 1])

# Part 3
def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)                  # i1 -> value: 4 & new_list: [5], i2 -> value: 9 & new_list: [5, 10], i3 -> value: 2 & new_list: [5, 10, 3], i4 -> value: 1 & new_list: [5, 10, 3, 2]
    return new_list

result = increment_all([4, 9, 2, 1])