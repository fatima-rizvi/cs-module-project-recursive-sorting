# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements # Creates a merged array that is composed only of zeroes and is as long as the combined length of arrA & arrB
    # Creating the array at a defined length beforehand is better for space and time complexity (at least a little)
    a_index = 0  # Using these to compare the arrays together, like pointers
    b_index = 0  # Using these to compare the arrays together, like pointers
    for i in range(len(merged_arr)):    # Iterate through the merged_arr, use rnage to get the index
        if a_index > len(arrA) - 1:     # Edge case: If arrA doesn't exist or if a_index has gone beyond the length of arrA
            merged_arr[i] = arrB[b_index]   # Set the current spot in merged_arr to the next value in arrB
            b_index += 1                    # Increment the b_index up by one
        elif b_index > len(arrB) -1:    # Edge case: If arrB doesn't exist or if b_index has gone beyond the length of arrB
            merged_arr[i] = arrA[a_index]   # Set the current spot in merged_arr to the next value in arrA
            a_index += 1                    # Increment the a_index up by one
        else:                           # If both arrA and arrB exist AND the index values haven't gone beyond the length of the arrays 
            if arrA[a_index] > arrB[b_index]:   # If the value at the current spot in the arrA is greater than the value in arrB 
                merged_arr[i] = arrB[b_index]   # Set the current spot in merged_arr to the next value in arrB
                b_index += 1    # Increment b_index up by one
            else:                       # If the value at the current spot the arrB is greater than the value in arrA 
                merged_arr[i] = arrA[a_index]   # Set the current spot in merged_arr to the next value in arrA
                a_index += 1    # Increment a_index up by one

    return merged_arr   # Return the merged array

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # We need to break up the array
    midpoint = len(arr) // 2 # To do that we need the midpoint
    left = arr[:midpoint]     # Keep track of the midpoints. This will grab everything before the midpoint, not including it
    right = arr[midpoint:]    # Keep track of the midpoints. This will grab everything after the midpoint, including the midpoint
    if len(left) > 1:   # Opposite of base case, keep doing this as long as the length of the left is greater than one
        left = merge_sort(left)    # Recurse on the left array, set the result into "left"
    if len(right) > 1:  # Opposite of base case, keep doing this as long as the length of the right is greater than one
        right = merge_sort(right)  # Recurse on the right array, set the result into "right"

    arr = merge(left,right)     # Magically assume there are a billion lefts and rights that will magically merge with this line. This uses the function we made above
    # Slightly better explanation of the line above: before we hit this line FOR THE LAST TIME, each of the times the function ran when we used recursion (lines 32 and 34) have already hit this line and merged their smaller left and right arrays. But the time we get to the final time this line will run, we just have two large left and right arrays.
    # Like, lines 28 through 34 will keep running until all of the teeny tiny left and right arrays are only one item long, then the rest of the function will keep running line 36 on those pairs of left and right arrays until we're back to one large array at the very end. FInally, we run line 40 and return a single, large array.

    return arr  # Return the final array

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
