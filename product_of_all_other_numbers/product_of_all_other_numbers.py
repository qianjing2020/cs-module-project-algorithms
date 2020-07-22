'''
Input: a List of integers
Returns: a List of integers
'''
import numpy as np

def product_of_all_other_numbers(arr):
    # return array of product of all numbers except the one at the index
    # initilize
    output = []
    # loop through array
    for idx, _ in enumerate(arr):
        # create a local copy lst
        lst = arr.copy()
        # pop the value at the idx
        lst.pop(idx)
        # return the product
        x = np.prod(lst)
        output.append(x)
    # return the product and update the value to the index
    return output


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
