def recursiveMultiply(m,n):
    if m < n:
        return recursiveMultiply(n,m)
    elif n!= 0:
        return (m + recursiveMultiply(m,n-1))
    else: 
        return 0
if __name__ == '__main__':
    print(recursiveMultiply(5,8))
