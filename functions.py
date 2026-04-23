# Double the value of a number.
# Input: a number to be doubled
# Result: a number
def double(n:int) -> int:
    result = n + n
    return result

# Answer to Question:
# No, if test_double_one had been the only testing function and passed, this wouldn't have meant the code was correct.
# The purpose of the function is to double a number, but the code was originally squaring a number instead.
# The value of 2 is able to pass the test because the result is 4 regardless of whether it is doubled or squared.
# The second testing function allowed us to see that the value of 3 was being squared and not doubled.
# Using additional testing functions that test values other than 2, zero or negative values, or extreme values would help us assess the code's logic.