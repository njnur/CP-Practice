def is_prime(number):
    """
    Finds the provided number Prime or Not
    Example No: 3.1 in Book
    Complexity: O(n)
    :param number: Number to be checked as Prime or Not
    :return: True / False
    """
    if number <= 1:
        return False
    else:
        for i in range(2, number-1):
            if number % i == 0:
                return False
        return True


import math


def is_prime_updated(number):
    """
    Finds the provided number Prime or Not
    Example No: 3.2 in Book
    Complexity: O(sqrt(n))
    :param number: Number to be checked as Prime or Not
    :return: True / False
    """
    if number <= 1:
        return False
    else:
        range_limit = int(math.sqrt(number))
        for i in range(2, range_limit):
            if number % i == 0:
                return False
        return True


if __name__ == '__main__':
    print(is_prime_updated(1068877))
