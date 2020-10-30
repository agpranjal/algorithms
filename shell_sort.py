arr = [3, 5, 7, 11, 13, 16, 18]

n = len(arr)//2
while n >= 1:
    i = 0
    j = i+n

    while j < len(arr):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        
        x = i
        while i-n >= 0:
            if arr[i-n] > arr[i]:
                arr[i], arr[i-n] = arr[i-n], arr[i]
            i -= 1
    
        j += 1
        i = x
        i += 1
    
    n //= 2

print(arr)
