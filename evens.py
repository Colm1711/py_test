def even_number_of_evens(numbers):
    """
    1. Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    2. if the list is empty it will return False
    3. if the number of even numbers is odd - return False
    4. if the numner of even numbers is even - return True
    """
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False
    else:
        raise TypeError("A list was not passed into the function")

if __name__ == '__main__':
    print(even_number_of_evens(5))