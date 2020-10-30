def create_heap(heap):
    for x in range(2, len(heap)):
        i = x

        while i > 1:
            if heap[i//2] < heap[i]:
                heap[i//2], heap[i] = heap[i], heap[i//2]
                i //= 2
            else:
                break

def delete_heap(heap, n):
    heap[1], heap[n] = heap[n], heap[1]
    n -= 1

    i = 1
    j = 2

    while j <= n:
        if j+1 <= n and heap[j] < heap[j+1]:
            j += 1

        if heap[j] > heap[i]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j *= 2
        else:
            break

def heap_sort(arr):
    heap = arr[:]
    heap = ["null"] + heap
    create_heap(heap)
    
    i = len(arr)
    while i >= 1:
        delete_heap(heap, i)
        i -= 1
        
    return heap[1:]

arr = [6, 5, 4, 3, 2, 1]
print(heap_sort(arr))

