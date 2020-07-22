'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # count occurence of each item
    counts = [arr.count(item) for item in arr] 
    # find index that have count value of 1
    idx = counts.index(1)
    # return array at this index
    return arr[idx]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")