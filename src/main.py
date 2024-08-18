from open_ai.writer import writer_request
from open_ai.image_creator import image_prompt_request, image_request

def main():
    while True:
        # Ask for a prompt
        prompt = input("Please enter a prompt: ")
        if prompt.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        # Request an instragram post based on the prompt
        post = writer_request(prompt)
        post_content = f"The following post has been generated:\n{post["content"]}"
        print(post_content)
        
        answer = input("Do you want to create an image for your post? [YES/NO]")
        answer = answer.lower()
        
        while not answer in ['yes', 'no']:
            answer = input("Answer was not yes or no. Do you want to create an image? [YES/NO]\n")
            answer = answer.lower()
        
        if answer == "yes":
            # Request a DALLE prompt based on the generated post 
            prompt = image_prompt_request(post["messages"])
            prompt_content = f"The following prompt has been generated for this post:\n{prompt["content"]}"
            print(prompt_content)
            
            # Generate image with DALLE based on prompt
            image_request(prompt["content"])
        
# This ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()