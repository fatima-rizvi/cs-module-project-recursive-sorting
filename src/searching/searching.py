# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # We need to set up a base case, which will be the way we exit the function. At what point do we want to exit? Should be simple and we should be moving towards it
    if end >= start:    # As long the end point is greater than or equal to the starting point, run the code below. Needs to include "=" because the target might be at that point
        midpoint = (start + end) // 2   # FInd the value of the midpoint, which is the sum of the start and the end divided by 2
        if target == arr[midpoint]: # Base case: If the taget is equal to the value in the array at the midpoint
            return midpoint     # Target found, return midpoint
        elif target > arr[midpoint]:    # If the target is greater than the value at the midpoint
            return binary_search(arr, target, (midpoint + 1), end)  # Recursion! Run the function but change the "start" to the midpoint - 1
        elif target < arr[midpoint]:     # If the target is less than the value at the midpoint
            return binary_search(arr, target, start, (midpoint - 1))    # Recursion! Run the function but change the "end" to the midpoint + 1
    return -1   # If the target doesn't exist in the array, return -1 (which is what the tests ask for)

[ 0, 1 ,     2 ,   3 , 4 , 5      , 6 , 7 , 8 , 9 , 10 ]

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
