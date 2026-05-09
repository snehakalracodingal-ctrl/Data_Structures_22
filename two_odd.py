def printTwoOdd(arr, size):
    # Step 1: XOR of all elements
    xorof2 = 0
    for i in range(size):
        xorof2 ^= arr[i]

    # Step 2: Get rightmost set bit
    setbit = xorof2 & ~(xorof2 - 1)

    # Step 3: Divide elements into two groups
    x = 0
    y = 0

    for i in range(size):
        if arr[i] & setbit:
            x ^= arr[i]
        else:
            y ^= arr[i]

    print("The two ODD elements are", x, "&", y)


# Input
arr = []
arr_size = int(input("Enter size of the array: "))

for i in range(arr_size):
    z = int(input("Enter element: "))
    arr.append(z)

printTwoOdd(arr, arr_size)