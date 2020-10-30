def TOH(n, A, B, C):
    if n == 0:
        return 0

    TOH(n-1, A, C, B)
    print(f"From {A} to {C}")
    TOH(n-1, B, A, C)

TOH(16, "A", "B", "C")
