def array_sum(arr,target):
    pairs = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if((arr[i]+arr[j]) == target):
                pairs.append((arr[i],arr[j]))
    return pairs

n=int(input("Enter the lenght of the array:"))
a = []
for i in range(n+1):
    a.append(int(input("Enter the Element in the array:")))
x = int(input("Enter the target element in the array:"))

print(array_sum(a,x))




