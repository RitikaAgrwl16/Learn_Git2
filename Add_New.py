def greet_user():
    # Ask the user for their name
    user_name = input("Enter your name: ")

    # Define greetings in different languages
    greetings = {
        'English': 'Hello, {}!',
        'Spanish': 'Hola, {}!',
        'French': 'Bonjur, {}!',
        'German': 'Hallo, {}!',
    }

    # Ask the user to choose a language
    print("Choose a language:")
    for i, language in enumerate(greetings.keys(), start=1):
        print(f"{i}. {language}")

    # Get user's language choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Validate the user's choice
    if 1 <= choice <= len(greetings):
        selected_language = list(greetings.keys())[choice - 1]
        greeting_message = greetings[selected_language].format(user_name)
        print(greeting_message)
    else:
        print("Invalid choice. Please choose a valid option.")

# Call the function to greet the user
greet_user()