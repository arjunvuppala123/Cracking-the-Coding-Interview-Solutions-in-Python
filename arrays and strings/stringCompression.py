import time

def stringCompression(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s + "1"
    else:
        compressed = ""
        count = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                compressed += s[i] + str(count)
                count = 1
        compressed += s[-1] + str(count)
        if len(compressed) >= len(s):
            return s
        else:
            return compressed

if __name__ == '__main__':
    start_time  = time.time()
    res = stringCompression("aabbcc")
    print(res)
    print("--- %s seconds ---" % (time.time() - start_time))
