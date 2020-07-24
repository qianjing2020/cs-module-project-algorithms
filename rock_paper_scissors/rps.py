import sys

# iterative method:
def rock_paper_scissors(n):
    # 1 player's possible 3 moves:
    basic_move = ['rock', 'paper', 'scissors']
    # 2 player's possbile movies:
    # initialize multiplayer's moves:
    x = basic_move.copy()
    # augament the matrix for more players
    i = 2
    while i <= n:
        x = [[item] for _ in range(3) for item in x]
        # len(x) is the number of all possible combinations
        #print(f'x is {x}')
        # update the list
        
        for idx in range(0, len(x)//3):
            x[idx].append(basic_move[0])
        for idx in range(len(x)//3, 2*len(x)//3):
            x[idx].append(basic_move[1])
        for idx in range(2*len(x)//3, len(x)):
            x[idx].append(basic_move[2])
        
        i += 1
    return x
    
"""
# use recursion
def rock_paper_scissors(n):
    # base case
    if n == 1:
      lst = ['rock', 'paper', 'scissors']
    
    for item in rock_paper_scissors(n-1): 
      new_iem = [item] [item]
      new_item 
"""   
    

# use python built in function
"""
from itertools import product
def rock_paper_scissors(n):
    x = ['rock', 'paper', 'scissors']
    result = list(product(x, repeat = 3))
    return result
    
    """
num_players = 4
result = rock_paper_scissors(num_players)
print(f'There are {len(result)} possible combination for {num_players} players:')
print(result)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
