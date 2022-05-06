def inner_search(arr, item, low, high):
        middle = ((high - low) // 2) + low

        if arr[middle] == "":
            left = middle - 1
            right = middle + 1
            while True:
                if left < low and right > high:
                    return None
                elif right <= high and arr[right] != "":
                    middle = right
                    break
                elif left >= low and arr[left] != "":
                    middle = left
                    break
                left -= 1
                right += 1
                
        if arr[middle] == item:
            return middle
        if arr[middle] > item:
            return inner_search(arr, item, low, middle - 1)
        if arr[middle] < item:
            return inner_search(arr, item, middle + 1, high)

def sparseSearch(arr, item):
    return inner_search(arr, item, 0, len(arr) - 1)

if __name__ == '__main__':
    arr = ["at","","","","ball","","","car","","","dad","","",""]
    print(sparseSearch(arr,"ball"))