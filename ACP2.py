def firstSetBit(n):
    if n == 0:
        return 0
    
    position = 1
    
    while n > 0:
        if n & 1:
            return position
        n = n >> 1
        position += 1
num = int(input("Enter number: "))
print("Position of rightmost set bit:", firstSetBit(num))