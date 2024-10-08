def coin_change(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    
    for coin in coins:
        for x in range(coin,amount+1):
            dp[x]=min(dp[x],dp[x-coin]+1)
            
    return dp[amount] if dp[amount]!=float('inf')else -1
def main():
    coins_input=input("Enter the denominations of the coins separated by spaces:")
    coins=list(map(int,coins_input.split(",")))
    amount=int(input("Enter the total amount of money: "))
    result=coin_change(coins,amount)
    print(f"The minimum number of coins needed to make up the amount {amount} is : {result}")
    
if __name__=="__main__":
    main()