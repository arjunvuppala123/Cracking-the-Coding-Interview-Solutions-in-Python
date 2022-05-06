import time

def urlify(s,stringlength):
    s = s.strip()
    return s.replace(' ','%20')

if __name__ == '__main__':
    start = time.time()
    s = 'Mr John Smith    '
    print(urlify(s,13))
    print(time.time() - start)