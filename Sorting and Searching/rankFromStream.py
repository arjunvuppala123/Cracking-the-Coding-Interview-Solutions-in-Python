def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def rankFromStream(target,stream):
    stream = list(stream)
    quickSort(stream)
    print("Array after sorting: ")
    printArray(stream)
    return stream.index(target)

def printArray(stream):
    print(stream)

if __name__ == '__main__':
    stream = []
    print("Enter the size of stream: ")
    n = int(input())
    print("Enter the stream: ")
    for i in range(n):
        stream.append(int(input()))
    print("Enter the target: ")
    target = int(input())
    print("Array before sorting")
    printArray(stream)
    print(rankFromStream(target,stream))