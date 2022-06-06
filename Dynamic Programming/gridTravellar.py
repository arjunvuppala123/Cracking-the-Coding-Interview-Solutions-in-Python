memo = {}
def gridTravellar(m,n):
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[key] = gridTravellar(m-1,n) + gridTravellar(m,n-1)
    return memo[key]
m = 2
n = 2
ans = gridTravellar(m,n)
print(ans)