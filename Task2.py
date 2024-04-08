"""
1. Filter names from list that starts with "a" or "A" using lambda function

· ["Alex", "Bob", "dan", "ash"] => ["Alex", "ash"]
"""

# arr = ["Alex", "Bob", "dan", "ash"]
# result = filter(lambda x: x[0] == 'a' or x[0] == 'A', arr)
# print(list(result))

"""
2. Use map() to get True for each value greater than 10 in a list of integers, else False

· [1,2,34,2,56] => [False, False, True, False, True]
"""
# arr = [1,2,34,2,56]
# result = map(lambda x: x > 10, arr)
# print(list(result))

"""
3. Create function to take arbitrary number of integer and return the average of those numbers

· average(1,2,4,5,6) => 3.6

· average(1,2,5,6) => 3.5
"""

# def average(*args):
#     return sum(args)/len(args)
# print(average(1,2,4,5,6))

"""
4. Create function accepts arbitrary number of keyword arguments and return dictionary with keys and values swapped as shown below

· get_values(a=1, b=2, e=3) => {1:'a', 2:'b', 3:'e'}

· get_values(a=1, b=2) => {1:'a', 2:'b'}
"""

# def get_values(**kwargs):
#     return {v:k for k,v in kwargs.items()}
# print(get_values(a=1, b=2, e=3))

"""
5. Create list compreshension for numbers between 1 to 20 whose square are even numbers

· [4,16,36, 64,100, 144, 196, 256, 324, 400]

"""

# print([ i*i for i in range(1,21) if i*i %2 ==0])

"""
6. Create dictionary with numbers as key and object as list of [square, cube] using comprehension for number as shown below
· {1: [1, 1], 2: [4, 8], 3: [9,27], 4: [16, 64]}
"""
nums = { i : [i*i,i*i*i] for i in range(1,5)}
print(nums)