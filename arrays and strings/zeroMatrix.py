import time

def zeroMatrix(x):
    row = []
    col = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                row.append(i)
                col.append(j)
    for i in row:
        for j in range(len(x[0])):
            x[i][j] = 0
    for j in col:
        for i in range(len(x)):
            x[i][j] = 0
    return x

if __name__ == '__main__':
    start_time  = time.time()
    x = [[1,2,3,4,5],[6,7,8,9,10],[11,12,0,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print(zeroMatrix(x))
    print("--- %s seconds ---" % (time.time() - start_time))