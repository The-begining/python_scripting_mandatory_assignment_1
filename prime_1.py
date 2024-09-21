import time 

def find_prime_factors(n, prime_factors=None):  
    start_time = time.time()  # Start the timer
    if prime_factors is None:
        prime_factors = []
    i = 2
    while i * i <= n: 
        if n % i == 0:
            prime_factors.append(i) 
            n //= i 
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    end_time = time.time()  # End the timer
    total_time = end_time - start_time  # Calculate elapsed time
    return prime_factors, total_time


print( find_prime_factors(1))
print( find_prime_factors(2))
print( find_prime_factors(50))
print( find_prime_factors(10000000000033))