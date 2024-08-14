def main():
    while True:
        # Ask for a prompt
        prompt = input("Please enter a prompt: ")
        if prompt.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        response = f"The prompt you entered is: {prompt}"

        # Print the response
        print(response)

# This ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()