import numpy as np

def diffBetweenTwoStrings(source, target):
    """
    @param source: str
    @param target: str
    @return: str[]
    """
    # Initialize table
    num_rows = len(source) + 1
    num_cols = len(target) + 1
    #dp = [num_cols * [0] for _ in range(num_rows)]
    dp = np.zeros(shape=(num_rows, num_cols))
    for i in range(num_rows):
        dp[i][0] = i
    for j in range(num_cols):
        dp[0][j] = j

    # Fill dp table
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            # Same letter
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # Modification
            else:
                dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]})

    # Determine path
    path = []
    i = num_rows - 1
    j = num_cols - 1
    import pdb; pdb.set_trace()
    while not (i == 0 and j == 0):
        min_val = min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]})

        # Keep source letter (diagonal)
        if (i > 0) and (j > 0) and (dp[i-1][j-1] == min_val) and (dp[i][j] == dp[i-1][j-1]):
            path = [source[i - 1]] + path
            i -= 1
            j -= 1

        # Add target letter (left)
        elif (j > 0) and (dp[i][j - 1] == min_val):
            path = ['+' + target[j - 1]] + path
            j -= 1

        # Subtract source letter (up)
        elif (i > 0) and (dp[i - 1][j] == min_val):
            path = ['-' + source[i - 1]] + path
            i -= 1

        # Subtract source and add target (diagonal)
        else:
            path = ['-' + source[i - 1]] + ['+' + target[j - 1]] + path
            i -= 1
            j -= 1

    return path

    """
  
    2 possibilities:
    1. add 1 to minimum of left, diag, up
    2. no change, use diagnol
  
      " s q u i r t l e
    " 0 1 2 3 4 5 6 7 8
    t 1 1 2 3 4 5 5 6 7
    u 2 2 2 2 3 4 5 6 7
    r 3 3 3 3 3 3 4 5 6
    t 4 4 4 4 4 4 3 4 5
    l 5 5 5 5 5 5 4 3 4
    e 6 6 6 6 6 6 5 4 3
  
    minimum is:
    left: add a (tgt) letter (if exists) 2.
    up: sub a (src) letter (if exists) 3.
    diag: keep (if exists)    1.
    diag+1: sub/add (src)/(tgt) (if exists) 4.
  
    -t +s +q u +i r t l e  # left first
    +s -t +q u +i r t l e   # diag first
    """

if __name__ == '__main__':
    path = diffBetweenTwoStrings('ABCDEFG', 'ABDFFGH')
    print(path)