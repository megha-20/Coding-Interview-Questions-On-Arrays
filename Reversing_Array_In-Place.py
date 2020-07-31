def reverse_array(A):

    # Pointer, pointing to first item of an array
    start_index = 0

    # Pointer, pointing to last item of an array
    end_index = len(A)-1

    # Termination condition, until start_index less than end_index
    while start_index < end_index:

        # Swap two items
        A[start_index], A[end_index] = A[end_index], A[start_index]  

        # Increment start_index
        start_index = start_index + 1

        # Decrement end_index
        end_index = end_index - 1

    # Reversed Array
    return A

if __name__ == "__main__":

    A = [1, 2, 3, 4, 5]
    print(reverse_array(A))

# Time - Complexity : O(N) [Linear time] 
