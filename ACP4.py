num = int(input("Enter your number : "))

count = 0
max_count = 0

while num > 0:
    if num & 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

    num = num >> 1

print("Longest consecutive 1's length : ", max_count)