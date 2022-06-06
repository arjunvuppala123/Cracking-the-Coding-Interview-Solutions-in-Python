def shouldSwap(string,start,end):
    for i in range(start,end):
        if string[i] == string[end]:
            return False
    else:
        return True

def permutation(string,index,n):
    if index >= n:
        print("".join(string))
        return
    
    for i in range(index,n):
        if shouldSwap(string,index,i):
            string[index],string[i] = string[i],string[index]
            permutation(string,index+1,n)
            string[index],string[i] = string[i],string[index]

if __name__ == '__main__':
    inp = input("Enter a string: ")
    inp = list(inp)
    n = len(inp)
    permutation(inp,0,n)
