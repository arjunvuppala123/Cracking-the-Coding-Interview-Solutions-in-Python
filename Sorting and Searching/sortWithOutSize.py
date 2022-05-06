def binarySearch(arr,left,right,target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr,left,mid-1,target)
    else:
        return binarySearch(arr,mid+1,right,target)

def findPos(arr,key):
    left,right,val = 0,1,arr[0]

    while val < key:
        left = right
        right = right * 2
        val = arr[right]
    
    return binarySearch(arr,left,right,key)

if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    print(findPos(arr,10))