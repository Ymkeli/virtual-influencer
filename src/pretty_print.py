'''Functions that help pretty print content'''

# Pretty print content when waiting for an API to respond
def print_wait(content):
    print()
    print("### " + content + " ###")
    print()
    
# Pretty print generated posts    
def print_post(content):
    print()
    print('-' * 70)
    print(content)
    print('-' * 70)
    print()

# Pretty print generated prompts for DALL-E    
def print_prompts(prompts):
    print()
    for idx, prompt in enumerate(prompts):
        print(f"{idx + 1}. *** {prompt["title"]} ***")
        print(prompt["content"])
        print()