import numpy as np
import time

iterations = 0

def nqueens(table, col, n):
    global iterations
    iterations += 1
    
    if col >= n:
        return True
    
    for i in range(n):
        if isSafe(table, i, col, n):
            table[i][col] = 1
            if nqueens(table, col+1, n):
                return True
            table[i][col] = 0
    return False
        
def isSafe(table, row, col, n):    
    # check row
    for i in range(col):
        if table[row][i] == 1:
            return False
    
    # check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if table[i][j] == 1:
            return False
    
    # check lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1,     -1)):
        if table[i][j] == 1:
            return False
    
    return True

def main():
    global iterations
    
    ns = [3,4,7,15,18]
    
    for n in ns:
        iterations = 0
        start = time.time()
        
        board = np.zeros((n,n), dtype=int)
        teste = nqueens(board, 0, n)
        
        print("\nn = ", n)
        print("Iterations: ", iterations)
        print("Time: ", time.time() - start)
        
        if (not teste):
            print("Solution does not exist")

if __name__ == "__main__":
    main()
