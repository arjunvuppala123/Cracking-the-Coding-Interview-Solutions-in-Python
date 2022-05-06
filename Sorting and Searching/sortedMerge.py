def sortedMerge(list1,list2):
    result = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result += list1
    result += list2
    return result

if __name__ == '__main__':
    list1 = [1,3,5,7]
    list2 = [2,4,6,8]
    print(sortedMerge(list1,list2))