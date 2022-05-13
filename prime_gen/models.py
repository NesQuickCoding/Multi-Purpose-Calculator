import random

def range_1_n(limit : int):
    """
    Finds all the prime numbers from 1 to <limit> (inclusive)
    Generates numbers based off of the Sieve of Atkin algorithm 
    ref: https://en.wikipedia.org/wiki/Sieve_of_Atkin

    Parameters
    ----------
    limit : int
        Precondition: limit must be a positive, non-zero integer
        Limit of the range

    Returns
    -------
    [int], [str]
        Final list of integers that are prime numbers
        If there are none, returns ["None"]
    """
    # Check for positive integer
    if limit <= 0:
        raise ValueError("Value must be a positive integer")

    # --- Initializers ---
    # Results list contains all prime numbers
    results = []

    # Check to see if limit is 1 (meaning no prime numbers)
    if limit == 1:
        return "[None]"
    # Otherwise, add the prime numbers manually up to 5
    else:
        if limit >= 2:
            results.append(2)
        if limit >= 3:
            results.append(3)
        if limit >= 5:
            results.append(5)
    
    # Potential list will store a the range from 1 to limit,
    # Each cell is the number and if it is marked prime or not
    # Starting off with every number marked not prime
    potentials = []
    for i in range(1, limit + 1):
        potentials.append([i, False])

    # --- Sieve of Atkin Implementation ---
    # Use all positive integers of x and y for finding possible solutions for n

    x = 1
    # Comparing the square of x prevents useless loops that would fail
    while x * x <= limit:
        y = 1
        # Comparing the square of y prevents useless loops that would fail
        while y * y <= limit:       
            # Condition 1:
            # remainder of n = 4x^2 + y^2 modulo 60 is 1, 13, 17, 29, 37, 41, 49, and 53
            # and where x is all numbers and y is odd
            n = (4 * x * x) + (y * y)
            if n <= limit and y % 2 == 1 and n % 60 in [1, 13, 17, 29, 37, 41, 49, 53]:
                potentials[n - 1][1] = True
            
            # Condition 2:
            # remainder of n = 3x^2 + y^2 modulo 60 is 7, 19, 31, 43
            # and where x is odd and y is even
            n = (3 * x * x) + (y * y)
            if n <= limit and x % 2 == 1 and y % 2 == 0 and n % 60 in [7, 19, 31, 43]:
                potentials[n - 1][1] = True
            
            # Condition 3:
            # remainder of n = 3x^2 - y^2 modulo 60 is 11, 23, 47, 59
            # and where x and y is an even/odd or odd/even combo
            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and y % 2 == (x - 1) % 2 and n % 60 in [11, 23, 47, 59]:
                potentials[n - 1][1] = True
            
            y += 1

        x += 1

    # --- Remove perfect squares from the potentials list
    for i in range(len(potentials)):
        if potentials[i][1]:
            power = potentials[i][0] * potentials[i][0]
            for j in range(power, limit, power):
                potentials[j][1] = False
    
    # --- Extract prime numbers from potentional list and output results
    for n in potentials:
        if n[1]:
            results.append(n[0])
    
    return results

def is_prime(n : int):
    """
    Determines if a number is prime or not
    
    Parameters:
    -----------
    n : int
        Precondition: n must be a positive integer
        Number to test if prime
    
    Returns
    -------
    Boolean
        True if n is prime, False if not
    """
    # Check for positive integer
    if n <= 0:
        raise ValueError("Value must be a positive integer")
    
    # Manually return 1 as False
    if n == 1:
        return False
    
    # Loop through integer i, starting at 2 and up until the square
    # of i is greater than the value of n
    # If n is divisable by i, n is not a prime number.
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def digit_size(digits : int, total : int):
    """
    Generate a set of random prime numbers by a digit size
    Will generate a number number that has <digits> amount of digits
    Then check if the number is prime
    This prime number generator will continue finding random prime numbers
    Until a <total> amount is found

    Parameters
    ----------
    digits : int
        number of digit places for each random number
        Precondition: must be positive, non-zero integer
    total : int
        how many random prime numbers to generate
        Precondition: must be positive, non-zero integer
    
    Returns
    -------
    [int]
        Results of randomly generated prime numbers
    """
    # Check for positive integer
    if digits <= 0 or total <= 0:
        raise ValueError("Argument values must be a positive integer")

    # --- Initializer ---
    results = []

    # --- Loop ---
    # Continues until the results list has <total> amount of entries
    while len(results) < total:
        # Create a random number from 1 * (digit size - 1) to 9 * Digit size
        number = random.randint(int("1" + ("0" * (digits - 1))), int("9" * digits))
        
        # If the number is prime, add it to results
        if is_prime(int(number)):
            results.append(int(number))

    return results
