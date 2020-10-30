class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

arr = [6, 8, 3, 10, 15, 6, 9, 12, 6, 3]
bins = [None]*(max(arr)+1)

for i in range(len(arr)):
    ptr = bins[arr[i]]
    if not ptr:
        bins[arr[i]] = Node(arr[i])
    else:
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(arr[i])

j = 0
for i in range(len(bins)):
    while bins[i]:
        arr[j] = bins[i].value
        bins[i] = bins[i].next
        j += 1

print(arr)

