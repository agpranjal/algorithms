arr = [6, 3, 9, 10, 15, 6, 8, 12, 3, 6]
count = [0]*(max(arr)+1)

for i in range(len(arr)):
    count[arr[i]] += 1

i = 0
j = 0

while i < len(arr):
    if count[j] > 0:
        arr[i] = j
        count[j] -= 1
        i += 1
        continue
    j += 1

print(arr)
    
