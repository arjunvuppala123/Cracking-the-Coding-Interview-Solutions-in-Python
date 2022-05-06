def oneAway(s1,s2):
    if s1==s2:
        return True

    m = len(s1)
    n = len(s2)

    if abs(m-n) > 1:
        return False
    
    count = 0

    i,j = 0,0

    while i < m and j < n:
        if s1[i] != s2[j]:
            if count == 1:
                return False
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1
            count += 1
        else:
            i += 1
            j += 1
    
    if i<m or j<n:
        count += 1
    return count == 1


if __name__ == '__main__':
    print(oneAway('arjun','arjn'))
    print(oneAway('arjun','arjunv'))
    print(oneAway('arjun','arjun'))
    print(oneAway('arjun','brjun'))
    print(oneAway('arjun','nnjun'))