'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # input: k: size of window
    # special case:
    if len(nums)<=k:
        return max(nums)
    else:
        # init output list
        output = [0]* (len(nums)-k+1)
        # slide window over and find max of window
        for idx, _ in enumerate(output):
            output[idx] = max(nums[idx:idx+k])
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
