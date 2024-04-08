"""
Q1. Create a generator-based method to print even numbers from 0 to 50.
"""
# def even(num):
#     curr = 0
#     while curr <= num:
#         if curr % 2 == 0:
#             yield curr
#         curr +=1

# gen_obj = even(50)
# for i in gen_obj:
#     print(i)

"""
Q2. Write a function my_enumerate that works like enumerate.
"""
# list_animals = ["Cat","Dog","Hog","Goat"]
# list_iterator = iter(list_animals)
# def my_enum(iterable_nums):
#     nums = 0
#     while True:
#         try:
#             yield nums, next(iterable_nums)
#             nums+=1
#         except:
#             break
#     pass
# gen_obj = my_enum(list_iterator)
# for i in gen_obj:
#     print(i)
"""
Q3. Write a program for finding factorial of a number using generators.
"""
# def factorial(num):
#     res = 1
#     curr = 0
#     while curr < num:
#         curr +=1
#         res *= curr
#     yield res
# gen_obj = factorial(3)
# print(next(gen_obj))

"""
Q4. We have a division method which throws exception when we divide a number by zero. We need to write a class-based decorator which works as exception handler for division method.

def division (number1, number2):

return number1/ number2
"""

# class Check:
#     def __init__(self,func):
#         self.func = func
#     def __call__(self, num1, num2):
#         if num2 == 0:
#             print("cannot divide by zero.")
#         else:
#             self.func(num1,num2)
# @Check    
# def div(num1,num2):
#     print(num1/num2)

# print(div(1,10))
"""
Q5. We have a list of mobile numbers. We need to sort those numbers in ascending order and then we need to print them in the standard format of (+91 xxxx xxx xxx). Create a function which performs sorting on mobile numbers and create a decorator which will convert these mobiles into standard format.

Sample Input: - [07895460981, 9711231230, 919711540230]

Sample Output: - [+91 7895 460 981, +91 9711 231 230, +91 9711 540 230]
"""

# sample = [9485763982,9485763922,7485763982,8485763982]
# res = []

# def convert(func):
#     #sorts the numbers
#     sample.sort()
#     def convert():
#         #converts the numbers
#         for i in sample:
#             res.append("+91"+str(i))
#         func()
#     return convert

# @convert
# def main():
#     print(res)

# main()