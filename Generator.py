#######################################
# Python Iterators and Generators 
#######################################
# Iterator
# An iterator is an object that lets you access items 
# in a sequence one at a time. It does not load the 
# entire data at once, instead it gives one value when 
# asked. This saves memory and follows lazy evaluation 
# (creates values only when needed).
# l = iter(['Geeks', 'For', 'Geeks'])
# print(next(l))
# print(next(l))
# print(next(l))
#########################
# Generators
# A generator is another way to create iterators, but 
# in a simpler and more readable manner. Instead of 
# storing all values, generators produce values on the 
# fly using the yield keyword.

# def sq_numbers(n):
#     for i in range(1, n+1):
#         yield i*i

# a = sq_numbers(3)

# print("The square of numbers 1, 2, 3 are:")
# print(next(a))
# print(next(a))
# print(next(a))
#########################################


# The Square Generator
# Create a generator function that yields the squares of numbers from 1 to n.

# def square_generator(n):
#     for i in range(1, n + 1):
#         yield i ** 2

# for square in square_generator(5):
#     print(square, end=" ")
    
################################################

# Even Number Iterator
# Write a class-based iterator that returns even numbers up to a specified limit.
# class EvenIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.limit:
#             raise StopIteration
#         value = self.current
#         self.current += 2
#         return value

# for num in EvenIterator(10):
#     print(num, end=" ")
    
######################################################### 
# Custom Range
# Re-implement a simplified version of the range() function using a generator.

# def custom_range(start, stop, step=1):
#     current = start
#     while current < stop:
#         yield current
#         current += step
# for num in custom_range(2, 10, 2):
#     print(num, end=" ")

##################################################
# Vowel Filter
# def vowel_filter(text):
#     vowels = "aeiou"
#     for char in text:
#         if char.lower() in vowels:
#             yield char

# for vowel in vowel_filter("Hello, World!"):
#     print(vowel, end=" ")
###################################################3
# Power of Two
# Write a generator expression (one-liner) that yields 
# powers of 2 (e.g., 1, 2, 4, 8…).
# n = int(input("Enter nth  "))
# powers = (2 ** i for i in range(n))

# for value in powers:
#     print(value, end=" ")
#####################################################
# Fibonacci 
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# for num in fibonacci(8):
#     print(num, end=" ")

################################################
# Manual Iteration

# numbers = [10, 20, 30]
# iterator = iter(numbers)

# while True:
#     try:
#         value = next(iterator)
#         print(value, end=" ")
#     except StopIteration:
#         break
###############################################

