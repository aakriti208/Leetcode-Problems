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