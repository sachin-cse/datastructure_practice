n = int(input())
arr = []
for i in range(n+1):
    arr.append(int(input()))
num = max(arr)
expected_sum = (num*(num+1))//2
actual_sum = sum(arr)
missing_number = expected_sum - actual_sum
print(missing_number)
