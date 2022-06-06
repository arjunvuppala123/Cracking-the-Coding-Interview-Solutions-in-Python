import time

def subsets(nums):
    res = [[]]
    for i in nums:
        temp = []
        for j in res:
            temp.append(j + [i])
        res += temp
    return res

if __name__ == '__main__':
    start = time.time()
    print(subsets([1,2,3,4,5,6,7,8,9,10]))
    end = time.time()
    print("Time elapsed: " + str(end - start))