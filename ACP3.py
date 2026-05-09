def reverse_bits(n):
    rev = 0  
    while n > 0:
        bit = n & 1          
        rev = (rev << 1) | bit   
        n = n >> 1              
    return rev
num = int(input("Enter number: "))
result = reverse_bits(num)
print("Reversed bits number:", result)