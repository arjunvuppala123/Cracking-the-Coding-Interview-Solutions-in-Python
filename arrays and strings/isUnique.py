import time

def isUnique(s):
    s = [char for char in s]
    uniq_char = set()
    for i in range(len(s)):
        if s[i] in uniq_char:
            return False
        else:
            uniq_char.add(s[i])
    return True 

if __name__ == '__main__': 
    start_time  = time.time()
    res = isUnique("op8ui")
    print(res)
    print("--- %s seconds ---" % (time.time() - start_time))