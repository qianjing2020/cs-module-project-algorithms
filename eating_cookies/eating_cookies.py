'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=[]):
    # input n cookies in the cookie jar
    # output numbero ways cookie monster can finish the jar
    # cookie monster can eat 1, or 2, or 3 cookies at one time
    # step 1: eat 1 or 2 or 3 cookies, so there are three branches (possible ways) for step 1
    # step 2: eat the leftover n-1, n-2, n-3 cookies, sum all three branches to get the total number of ways to eat n cookies
    # this can be recursively solved
    # base case: 0 cookie, 1 ways this is trick, because the end branch leading to 0 cookies shoiuld stay as one way, not 0
    if len(cache) == 0:  # this is the same as cache == [], but not the same as cache is None
        cache = [0 for _ in range(0, n+1)]

    if n == 0:
        cache[0] = 1        
       
    # base case: 1 cookie, 1 way
    if n == 1:
        cache[1] = 1
    
    # base case: 2 cookies, 2 ways (1+1, or 2)
    if n == 2:
        cache[2] = 2
                
    # if the case has been run and saved as cache
    if cache[n] != 0:
        #print(cache)
        return cache[n]

    # recursive cases:    
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache) 
        
    return cache[n] 


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 20
    ways = eating_cookies(num_cookies)#, [0 for _ in range(num_cookies+1)])
    print(f"There are {ways} ways for Cookie Monster to each {num_cookies} cookies")
