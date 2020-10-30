arr = [8, 5, 7, 3, 2]

for i in range(len(arr)):
    flag = True
    ls = []
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = False
    print(arr)

    print(ls)

    if flag:
        break

print(arr)

