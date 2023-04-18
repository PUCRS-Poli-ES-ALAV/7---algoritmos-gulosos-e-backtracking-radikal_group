import time

iterations = 0

def Sort_Tuple(tup_list):
    # getting length of list of tuples
    lst = len(tup_list)
    for i in range(0, lst):
 
        for j in range(0, lst-i-1):
            if (tup_list[j][1] > tup_list[j + 1][1]):
                temp = tup_list[j]
                tup_list[j] = tup_list[j + 1]
                tup_list[j + 1] = temp
    return tup_list

def sdm_greedy(s: list[int], f: list[int]) -> list[int]:
    global iterations
    f = [-1] + f
    s = [-1] + s
    x = []
    i = 0
    for k in range(1,len(s)):
        iterations += 1
        if s[k] > f[i]:
            x.append(k-1)
            i = k
    return x

def main():
    global iterations
    
    iterations = 0

    s = [4, 6, 13, 4, 2, 6, 7,  9,  1, 3,  9]
    f = [8, 7, 14, 5, 4, 9, 10, 11, 6, 13, 12]
    
    tup_list = [(x,y) for x,y in zip(s,f)]
    tup_list = Sort_Tuple(tup_list)
    
    s = [x[0] for x in tup_list]
    f = [x[1] for x in tup_list]
    
    start = time.time()
    x = sdm_greedy(s, f)
    print("\n",s,"\n",f,"\n",x,"\n")
    
    print("Iterations: ",iterations)
    print("Time: ",time.time()-start)

if __name__ == "__main__":
    main()
        