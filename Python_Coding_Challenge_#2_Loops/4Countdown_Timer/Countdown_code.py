# Start countdown from 10
num = 10

while num > 0:
    print(num)  # Print the current number
    user_input = input('Enter "stop" to cancel or press Enter: ')  # Ask user if they want to stop

    if user_input.lower() == "stop":  # Check if the user typed "stop"
        print("Countdown stopped!")
        break  # Exit the loop

    num -= 1  # Decrease the counter
