arr = [1, 3, 4, 2, 2, 5]
a = []

for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            a.append(arr[i])
if len(arr)==0:
    print("no duplicate elements")
else:
    print(f'duplicate element is {a}')
    