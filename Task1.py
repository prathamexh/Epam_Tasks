'''
1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

input: 34,67,55,33,12,98

output:

['34', '67', '55', '33', '12', '98']
'''
# inp = input()
# list1 = [ i for i in inp.split(",")]
# tuple1 = tuple(list1)
# print(list1,tuple1)

'''
2. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

input:

hello world and practice makes perfect and hello world again

output:

again and hello makes perfect practice world
'''
# inp = input()
# hm = list({i for i in inp.split(" ")})
# hm.sort()
# print(" ".join(hm))

"""
3. Write a program that accepts a sentence and calculate the number of upper-case letters and lower-case letters.

input:

Hello world!

output:

UPPER CASE 1

LOWER CASE 9
"""
# Upper = 0
# Lower = 0
# s = input()
# for i in s:
#     if ord(i) >= 97 and ord(i) <= 122:
#         Lower += 1
#     elif ord(i) >= 65 and ord(i) <= 90:
#         Upper += 1
# print("Upper", Upper)
# print("Lower", Lower)

"""
4. Write a method which accepts a list of numbers and return a list containing square of each odd number. Use list comprehension.

Input:

[1,2,3,4,5,6,7,8,9]

Output:

[1,3,25,49,81]
"""
# inp = input()
# list1 = [int(i) for i in inp.split(",")]
# res = []
# for i in list1:
#     if i % 2 != 0:
#         res.append(i*i)
# print(res)
"""
5. Write method which accepts a list of integers nums and an integer result, return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], result= 9

Output: [0,1]

Explanation: from nums, 2+7 = 9 ie. result. Thus, the output is indices of 2 and 7 i.e. [0,1]

Input: nums = [3,2,4], result= 6

Output: [1,2]

Explanation: 2+4 = 6 thus output is indices of 2 and 4 i.e. [1,2]
"""
# nums = [3,2,4]
# result = 6
# hm = {}
# for i in range(len(nums)):
#     if nums[i] in hm:
#         print(hm[nums[i]], i )
#     else:
#         hm[result - nums[i]] = i
