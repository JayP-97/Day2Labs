
user_input = int(input("Enter an integer between 1 and 100 inclusive: "))

if 1 <= user_input <= 100:

        if user_input % 2 != 0 and user_input < 60:
                print(f"{user_input}: Odd and less than 60.")
        elif user_input % 2 == 0 and 2 <= user_input <= 24:
                print("Even and less than 25.")
        elif user_input % 2 == 0 and 26 <= user_input <= 60:
                print("Even and between 26 and 60 inclusive.")
        elif user_input % 2 == 0 and user_input > 60:
                print(f"{user_input}: Even and greater than 60.")
        elif user_input % 2 != 0 and user_input > 60:
                print(f"{user_input}: Odd and greater than 60.")
        else:
            print("Invalid input. Please enter an integer between 1 and 100 inclusive.")

# user_continue = input("Do you want to continue? (y/n): ").lower()
# if user_continue != 'y':
#      break