
# 1

# def generator(N):
#     for i in range(N):
#         yield i*i

# a = generator(10)
# for i in a:
#     print(i)

# 2

# def even_numbers(n):
#     for i in range(1,n):
#         if i % 2 == 0:
#             yield i

# print(",".join(str(num) for num in even_numbers(int(input("Enter a number: ")))))

# 3

# def div_by_3_4(n):
#     for i in range(n+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# for num in div_by_3_4(100):
#     print(num)

# 4

# def squares(a, b):
#     for i in range(a, b+1):
#         yield i**2

# for sq in squares(1, 5):
#     print(sq)

# 5

# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# for num in countdown(5):
#     print(num)
