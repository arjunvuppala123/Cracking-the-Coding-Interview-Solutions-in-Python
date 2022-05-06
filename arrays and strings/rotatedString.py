import time

def rotateString(s1,s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    s1 = s1 + s1
    return s2 in s1

if __name__ == '__main__':
    start_time  = time.time()
    s1 = "abcde"
    s2 = "cdeab"
    print(rotateString(s1,s2))
    print("--- %s seconds ---" % (time.time() - start_time))