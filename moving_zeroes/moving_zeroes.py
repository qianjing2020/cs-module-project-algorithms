'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # move nonzeros to the left of the arr
    # initialize output array
    altered_arr = [0 for item in arr]
    # find nonzeros
    nonzeros =[item for item in arr if item is not 0]
    # update output array with nonzero values
    altered_arr[0:len(nonzeros)] = nonzeros
    return altered_arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")