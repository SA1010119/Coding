# Loop through numbers 1 to 10
for num in range(1, 11):
    if num % 2 == 0:  # Check if the number is even
        continue  # Skip the even number and go to the next iteration
    print(num)  # Print only odd numbers
