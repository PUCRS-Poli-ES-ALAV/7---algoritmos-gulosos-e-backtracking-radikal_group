import numpy as np

iterations = 0

def nqueens(table, n):
    global iterations
    aux_i = 0
    aux_j = 0
    num_queen = 1
    while (num_queen < n):
        num_queen = 1
        while (aux_i< n):
            while (aux_j<n):
                table[aux_i][aux_j] = 2
                for i in range(n):
                    for j in range(n):
                        
                        if table[i][j] == 0:
                            table = setOccupied(table, i, j, n)
                            table[i][j] = 2
                            num_queen += 1
                aux_j += 1
            aux_i += 1


def set1Queen(table, i, j,n):
    setOccupied(table, i, j, n)
    table[i][j] = 2
    
def setOccupied(table, i, j, n):
    
    table[i] = 1
    table[:, j] = 1
    #diag_idx = np.diag_indices(i, j)
    #print (diag_idx)
    #table[diag_idx] = 1

    c = 0
    v = 0
    
    while (c<n and v<n):
        
        if (c-i>=0 and v-j>=0):
            if not2(table, i, j, c, v,1):
                table[c-i][v-j] = 1

        if (c+i<n and v-j>=0):
            if (not2(table,i,j,c,v,2)):
                table[c+i][v-j] = 1

        if (c-i>=0 and v+j<n):
            if not2(table, i, j, c, v,3):
                table[c-i][v+j] = 1

        if (c+i<n and v+j<n):
            if (not2(table,i,j,c,v,4)):
                table[c+i][v+j] = 1
        v+= 1
        c+= 1
    return table
def not2(table,i,j,c,v,typeM):
    if (typeM==1):
        if (table[c-i][v-j] == 2):
            return False
    elif (typeM==2):
        if (table[c+i][v-j] == 2):
            return False
    elif (typeM==3):
        if (table[c-i][v+j] == 2):
            return False
    elif (typeM==4):
        if (table[c+i][v+j] == 2):
            return False
    return True
def main():
    global iterations
    iterations = 0
    
    n = 7
    table = np.zeros((n, n), dtype=int)
    nqueens(table, n)
    #set1Queen(table,3,3,n)
    
    # print matrix
    for row in table:
        for col in row:
            if col == 2:
                print('Q', end=" ")
            else: 
                print(col, end=" ")
        print()

if __name__ == "__main__":
    main()
