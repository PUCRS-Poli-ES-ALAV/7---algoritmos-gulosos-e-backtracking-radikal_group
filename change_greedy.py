import time

available_coins = [[100, 50, 25, 10, 5, 1], [37,15,7,4,3], [98, 40, 26, 11, 6, 2]]
test_cases = [(1000,289), (500, 145), (414, 123)]
iterations = 0
    
def brute_force(cost: int, paid: int, coin_set: list[int]) -> list[int]:
    global iterations
    change = cost - paid
    change_coins = []
    
    for coin in coin_set:
        while change >= coin:
            iterations += 1
            
            change_coins.append(coin)
            change -= coin
    return change_coins

def count_coin_types(change: list[int], coin_set) -> list[int]:
    # Initialize a list of tuples with the coin value and the number of coins
    count_coins = []
    for coin in coin_set:
        count_coins.append((coin, 0))
    
    for i, coin in enumerate(coin_set):
        value = change.count(coin)
        count_coins[i] = value
    
    return count_coins

def main():
    global iterations
    for coin_set in available_coins:   
        for case in test_cases:
            print("\nCost:", case[0], "Paid:", case[1])
            iterations = 0
            cost = case[0]
            paid = case[1]
            
            start = time.time()
            # List of coins from change
            change_coins = brute_force(cost, paid, coin_set)
            end = time.time()
            
            change_value = sum(change_coins)
            
            # List with the number of coins of each type
            change_coins_count = count_coin_types(change_coins,coin_set)
            
            for i in range(len(change_coins_count)):
                if (i == len(change_coins_count)-1):
                    print (coin_set[i], "x", change_coins_count[i])
                    break
                if (change_coins_count[i]!= 0):
                    print (coin_set[i], "x", change_coins_count[i], ",", end=" ")
                

            unpaid_change = cost - paid - change_value
            if (unpaid_change != 0):
                print ("Unpaid Change", unpaid_change)
                
            print("Iterations:",iterations)
            print("Time:", end - start, "seconds\n")

if __name__ == "__main__":
    main()
    