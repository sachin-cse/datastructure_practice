arr = [5, 3, 8, 2, 9, 1]

largest = arr[0]
smallest = arr[0]

for i in range(1,len(arr)):
    if arr[i]>largest:
        largest = arr[i]
    elif arr[i] < smallest:
        smallest = arr[i]
print(largest)
print(smallest)
