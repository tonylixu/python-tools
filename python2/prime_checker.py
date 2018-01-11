'''
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it's Prime or Not prime.

1 <= T <= 30
1 <= n <= 2 x 10^9
'''

def check_if_prime(num):
    # Make sure n is a positive integer
    num = abs(num)
    # 0 and 1 are not primes
    if num < 2:
        return False
    # 2 is the only even prime number    
    if num == 2:
        return True
    # All even numbers are not prime
    if not num & 1:
        return False
    
    # If the square root is not a prime number,
    # Then the number is not
    if num > 2:
        for x in range(3, int(num**0.5) + 1, 2):
            if not num % x:
                return False
    else:
        return False
    
    return True

length = int(raw_input())
for i in range(length):
    num = int(raw_input())
    if check_if_prime(num):
        print "Prime"
    else:
        print "Not prime"