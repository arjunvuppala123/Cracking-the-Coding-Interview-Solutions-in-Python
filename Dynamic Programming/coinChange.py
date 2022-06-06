def coinChange(coins,amount):
    dp = [[0]*(amount+1)]*(len(coins)+1)
    for i in range(len(coins)):
        dp[i][0] = 1
    for j in range(amount):
        dp[0][j] = 0
    for i in range(len(coins)):
        for j in range(amount):
            if(coins[i-1]>j):
                dp[i][j] = dp[i-1][j]
            elif (coins[i-1]<=j):
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    print(dp)
    return dp[len(coins)][amount]

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    res = coinChange(coins,amount)
    print(res)