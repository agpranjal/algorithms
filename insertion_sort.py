arr = [8, 5, 7, 3, 2]

i = 1
while i < len(arr):
    j = i-1
    x = arr[i]
    
    while j >= 0 and arr[j] > x:
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = x
    i += 1

print(arr)

