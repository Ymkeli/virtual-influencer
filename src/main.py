from open_ai.writer import writer_request

def main():
    while True:
        # Ask for a prompt
        prompt = input("Please enter a prompt: ")
        if prompt.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        message = writer_request(prompt)
        response = f"The following message has been generated:\n{message}"

        # Print the response
        print(response)

# This ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()