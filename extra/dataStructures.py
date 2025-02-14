#Arrays

arr = [1,2,3,4] 
arr.append(6)   #insert O(n)
arr.pop()       #delete at end O(1)
arr.remove(3)   #delete by value O(n) 


#Linked List

#first define the node of the linkedlist
class Node:
    def __init__(self, data):
        self.data = data            #stores the value
        self.next = None            #pointer to the next node

#we define the linkedlist structure
class LinkedList:
    def __init__(self):
        self.head = None    #initially the list is empty. the head keeps track of the first node in the list

#we insert a node at the head
    def insert_at_head(self, data):
        new_node = Node(data)   #create a new node with the data
        new_node.next = self.head   #the new node points to the current head
        self.head = new_node        #update the head pointer

#printing the linkedlist
    def print_list(self):
        current = self.head     #start from the head
        while current:          #visit nodes until the end
            print(current.data, end="->")       #Print the current node's data
            current = current.next              #move to the next node
        print("None")            #indicated end of the list



# Stack : All O(1)

stack = []
stack.append(1)     #push 
stack.pop()         #pop
print(stack[-1])    #peek


#Queue : All O(1)

from collections import deque
q = deque()
q.append(1)     #enqueue
q.popleft()     #dequeue
print(q[0])     #peek


#Hashmap : All O(1)

hashmap = {}
hashmap["key1"] = 100
print(hashmap.get("key1"))   #search
hashmap.pop("key1")          #delete


# Sorting 

#MergeSort (O(nlogn))

def merge_sort(arr):
    #base case: arr already sorted
    if len(arr) <= 1:
        return arr
    
    #step 1 : Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    #step 2 : Marge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    l = r = 0
    
    #Step 3 : we compare the elements from both halves and merge them
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_arr.append(left[l])
            l += 1
        else:
            sorted_arr.append(right[r])
            r += 1
    #step 4 : append any remaining elements

    sorted_arr.append(left[l:])
    sorted_arr.append(right[r:])

    return sorted_arr



#Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1