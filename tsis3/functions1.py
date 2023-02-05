# 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
# 2 
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
# 3

# 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

numbers = [3,4,5,6,5,23]
prime_numbers = filter_prime(numbers)
print(prime_numbers)

# 5


