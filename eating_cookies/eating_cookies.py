'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # input n cookies in the cookie jar
    # output numbero ways cookie monster can finish the jar
    # cookie monster can eat 1, or 2, or 3 cookies at one time
    # step 1: eat 1 or 2 or 3 cookies, so there are three branches (possible ways) for step 1
    # step 2: eat the leftover n-1, n-2, n-3 cookies, sum all three branches to get the total number of ways to eat n cookies
    # this can be recursively solved
    # base case: 0 cookie, 1 ways this is trick, because the end branch leading to 0 cookies shoiuld stay as one way, not 0
    if n == 0:
        return 1 
    # base case: 1 cookie, 1 way
    if n == 1:
        return 1
    # base case: 2 cookies, 2 ways (1+1, or 2)
    if n == 2:
        return 2
    # base case: 3 cookies, 4 ways (1+1+1, 1+2, 2+1, 2+2)
    if n == 3:
        return 4
    
    # recursive cases:    
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)  


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
