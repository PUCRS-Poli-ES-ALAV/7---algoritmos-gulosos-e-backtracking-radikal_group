import numpy as np

iterations = 0

def nqueens(table, n):
    global iterations
    
    i = 2
    j =3
    setOccupied(table, i, j, n)
    table[i][j] = 52
    # for i in range(n):
    #     for j in range(n):
    #         if table[i][j] == 0:
    #             setOccupied(table, i, j, n)
    #             table[i][j] = 2

def setOccupied(table, i, j, n):
    table[i] = 0
    table[:, j] = 0
    
    np.fill_diagonal(table[i:,j:], 0)
    np.fill_diagonal(table[:i,:j], 0)
    np.fill_diagonal(np.fliplr(table[i:,:j+1]), 0)
    np.fill_diagonal(np.fliplr(table[:i+1,j:]), 0)
    
def main():
    global iterations
    iterations = 0
    
    n = 7
    table = np.arange(n*n).reshape(n,n)
    nqueens(table, n)
    
    # print matrix
    print()
    for row in table:
        for col in row:
            if col == 52:
                print('Q', end="  ")
            elif col < 10: 
                print(col, end="  ")
            else:
                print(col, end=" ")
        print()

if __name__ == "__main__":
    main()
