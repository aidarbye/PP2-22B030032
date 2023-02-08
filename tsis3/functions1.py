# 1

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
# 2 

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# 3

def solve(numheads,numlegs):
    chicks  = 0
    rabbits = 0
    if numlegs % 2 != 0:
        print("No solution")
    else:
        rabbits = (numlegs - 2 * numheads) / 2
        chicks = numheads - rabbits
        print(f"There are {int(chicks)} chickens and {int(rabbits)} rabbits")

# solve(35,94)

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

# 5
# first method
from itertools import permutations
def allPermutations(S):
    perm_arr = permutations(S)
    return ["".join(i) for i in perm_arr]

# print(allPermutations("ABC"))

# second method

# def ultra_shuffle(S):
#     lenght = len(S)
#     partial = []
#     partial.append(S[0])  
#     for i in range (1, lenght):
#         for j in range(len(partial) - 1, - 1, - 1):
#             curr = partial.pop(j)
#             for k in range(len(curr) + 1):
#                 partial.append(curr[:k] + S[i] + curr[k:])
#     print(partial)


# 6

def justReverse(s):
    new = []
    stroka = ""
    for i in range(len(s)):
        if s[i] == " ":
            new.append(stroka)
            stroka = ""
        elif i == len(s) - 1:
            new.append(stroka + s[i])
        else:
            stroka += s[i]
    print(new[::-1])


# 7 

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# 8 
def spy_game(nums):
    for i in range(len(nums) - 3):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i + 2] == 7:
            return True
    return False

# 9
def sphere_volume(radius):
  return (4/3) * 3.14 * (radius ** 3)

# 10
def gigaset(arr):
  G_set = []
  for i in arr:
    if i not in G_set:
      G_set.append(i)
  return G_set

# 11
def is_palindrome(word):
  word = word.lower().replace(" ", "")
  return word == word[::-1]

# 12

def histogram(arr):
  for i in arr:
    print("*" * i)

# 13
import random
def Game():
    print("Hello! What is your name?")
    name = input()

    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    print(f"Good job, {name} ! You guessed my number in {guesses} guesses!")