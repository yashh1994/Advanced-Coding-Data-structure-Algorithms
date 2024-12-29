def lps(pattern):
    arr = [0]*len(pattern)
    i,length = 1,0
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            arr[i] = length
            i += 1
        else:
            if length == 0:
                i += 1
            else:
                length = arr[length-1]
    print(arr)
    return arr

lps("AABAAA")


