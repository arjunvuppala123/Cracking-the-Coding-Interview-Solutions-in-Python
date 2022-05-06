import time

def isPermutation(s1,s2):
    if len(s1)!=len(s2):
        return False
    return sorted(s1) == sorted(s2)

if __name__ == '__main__':
    start_time  = time.time()
    res = isPermutation("vabp","abv")
    print(res)
    print("--- %s seconds ---" % (time.time() - start_time))
