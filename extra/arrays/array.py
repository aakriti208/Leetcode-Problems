class Solution:

    # Given an array of integers, return a new array where each element is the square of the original element.
    # def array_examples(self):
    #     array = [1, 2, 3, 4, 5]
    #     new_array = []
    #     for x in array:
    #         x = x*x
    #         new_array.append(x)
    #     print(new_array)

    # # Given an array of integers, return a new array where each element is the square of the original element.
    # def array_examples(self):
    #     array = [1, 2, 3, 4, 5]
    #     new_array = [x*x for x in array]
    #     print(new_array)

    # def array_filetring(self):
    #     array = [1, 2, 3, 4, 5]
    #     new_array = [x for x in array if x % 2 == 0]
    #     print(new_array)

    def reverse(self):
        array = [1, 2, 3, 4, 5]
        for i in range(len(array) - 1, -1, -2):
            print(array[i])
        
if __name__ == "__main__":
    solution = Solution()
    solution.reverse()
    
    
    from array import *

numbers = [5,4,3,6,9,10,23]


# List comprehension 
squares = [x//2 if x > 5 else x == 0 for x in numbers] 
print(squares)






# for using list methods

# for i, num in enumerate(numbers):
#     # numbers.pop()
#     print(numbers[i])
#     print(num)
    
# numbers.pop(1)
# numbers.insert(3, 99 )  
# print(numbers)
# numbers.count(6)


# only for printing or accessing elements : 

# for val in numbers:
#     print(val)

# accessing and slicing 
# print(numbers[2])
# print(numbers[-3])

# for i in range(len(numbers)+1):
#     print(numbers[-i])
    
# print(numbers[1:4])
# print(numbers[1:])
# print(numbers[:3])
# print(numbers[::4])

# Reverses the array
# print(numbers[::-1])

