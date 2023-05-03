def intro():
    print("Welcome to the school cafe app!")
    while True:
        try:
            age = int(input("Please enter your age (This programme is for students aged 13-18): "))
            if age < 13 or age > 18:
                print("Sorry, this app is only available for students aged 13-18.")
                exit()
            break  # if age is valid, exit the loop
        except ValueError:
            print("Invalid input. Please enter a valid number. eg 13 or 15")
    print("Please log in or create an account to use the app.")

intro()