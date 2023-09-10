
# Define the function list_divide
def list_divide(numbers, divide=2):
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count

# Define the custom exception class ListDivideException
class ListDivideException(Exception):
    pass

# Define the function test_list_divide
def test_list_divide():
    if list_divide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException("Test 1 failed")
    if list_divide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException("Test 2 failed")
    if list_divide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException("Test 3 failed")
    if list_divide([]) != 0:
        raise ListDivideException("Test 4 failed")
    if list_divide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException("Test 5 failed")

# Run the test function
test_list_divide()
