def remove_duplicate(arr):
    length = len(arr)
    for i in range(length):
        j = i+1
        while j<length:
            if arr[i] == arr[j]:
                arr.pop(j)
                length-=1
            else:
                j+=1
    return arr

arr = [1,1,2,3,4,5]
print(remove_duplicate(arr))

