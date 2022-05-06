def swap(arr1,arr2):
    temp = arr1
    arr1 = arr2
    arr2 = temp

def peaksAndValleys(arr):
    for i in range(1,len(arr),2):
        if arr[i - 1] < arr[i]:
            arr[i-1],arr[i] = arr[i],arr[i-1]
        if i + 1 < len(arr) and arr[i + 1] < arr[i]:
            arr[i+1],arr[i] = arr[i],arr[i+1]

if __name__ == '__main__':
    arr = [5,3,1,2,3]
    peaksAndValleys(arr)