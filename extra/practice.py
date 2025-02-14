# Arrays and Strings

# class Solution:
#     def iterateOverArray(self, arr):
#         arr = [1,2,3,4,5]
#         for i in arr:
#             print(i)    

    
#     def iterateOverArrayReverse(self, arr):
#         arr = [1,2,3,4,5,6,7,8]
#         n = len(arr)
#         for i in range(n,0,-1):
# 	        print(i)
             
#    # fetch every second element

#     def isPrime(self, arr):
#         arr = [1,2,3,4,5,6,7,8,9,10]
#         n = len(arr)
#         if arr > 2:
#             return False
#         for x in range(2, int(math.sqrt(n))):
#             if arr % x == 0:
#                 return False
#         return True
    
    
# Find first prime number in the array

# import math

# def isPrime(n):
#     if n < 2:
#         return False
#     for x in range(2, int(math.sqrt(n))+1):
#         if n % x == 0:
#             return False
#     return True

# def first_prime(arr):
#     for num in arr:
#         if isPrime(num):
#             return num
#     return None

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("First prime: ", first_prime(arr))



# def sumOfArray(arr):
#     sum = 0
#     for x in arr:
#         sum = sum + x
#     return sum

# arr = [[1,2,3,4,5,6]]
# print("Sum is", sumOfArray(arr))


class Solution:

    # Given an array of integers, return a new array where each element is the square of the original element.
    def array_examples(self):
        array = [1, 2, 3, 4, 5]
        new_array = []
        for x in array:
            x = x*x
            new_array.append(x)
        print(new_array)

    # Given an array of integers, return a new array where each element is the square of the original element.
    def array_examples(self):
        array = [1, 2, 3, 4, 5]
        new_array = [x*x for x in array]
        print(new_array)


if __name__ == "__main__":
    solution = Solution()
    solution.array_examples()
