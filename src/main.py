from open_ai.writer import writer_request
from open_ai.image_creator import image_prompt_request, image_request
from pretty_print import print_post, print_prompts, print_wait
from errors import FunctionError

def main():
    while True:
        # Ask for a prompt
        prompt = input("Please enter a prompt: ")
        if prompt.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        # Request an instragram post based on the prompt
        print_wait("A post is being generated...")
        post = writer_request(prompt)
        print("The following post has been generated:")
        print_post(post["content"])
        
        answer = input("Do you want to create images for your post? [YES/NO]\n")
        answer = answer.lower()
        print()
        
        while not answer in ['yes', 'no']:
            answer = input("Answer was not yes or no. Do you want to create an image prompt? [YES/NO]\n")
            answer = answer.lower()
        
        if answer == "yes":
            # Request DALLE prompt(s) based on the generated post
            print_wait("A prompt for DALLE is being generated...") 
            try:
                prompts = image_prompt_request(post["messages"])
            except FunctionError as e:
                print(f"Error: {e}")
                
            print("The following prompt has been generated for this post:")
            print_prompts(prompts)
            
            img = input("Do you want to create images for these prompts? [YES/NO]\n")
            
            if img.lower() == "yes":
                # Generate image(s) with DALL-E based on prompt
                print_wait("Image(s) are being generated by DALLE...")
                image_request(prompts)
        
# This ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()