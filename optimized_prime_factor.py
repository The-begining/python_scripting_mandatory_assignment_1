import time
def find_prime_factors(n):
    start_time = time.time()  # Start the timer
    prime_factors = []
    
    # Handle factor of 2 separately
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    
    # Check odd factors starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n //= i
        i += 2  # Increment by 2 to skip even numbers
    
    # If n is still greater than 1, it must be prime
    if n > 1:
        prime_factors.append(n)
    
    end_time = time.time()  # End the timer
    total_time = end_time - start_time  # Calculate elapsed time
    return prime_factors, total_time

print( find_prime_factors(1))
print( find_prime_factors(2))
print( find_prime_factors(50))
print( find_prime_factors(10000000000033))