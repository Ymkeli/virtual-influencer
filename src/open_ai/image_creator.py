from open_ai.request import query_open_ai_with_tools, query_dalle, format_content
import open_ai.tools as tools
from errors import FunctionError
from datetime import datetime
import requests
import json

IMAGE_QUERY = "Can you return 4 different prompts for DALLE based on this instagram post? Every prompt should be about a different aspect of the original post. Keep it short and compact."

# Request several prompts for DALL-E based on the generated post
def image_prompt_request(messages):
    user_content = format_content("user", IMAGE_QUERY)
    messages.append(user_content)
    response_function = query_open_ai_with_tools(messages, [tools.dalle_prompts])
    if response_function.name == "get_prompts":
        arguments = json.loads(response_function.arguments)
        return arguments["prompts"]
    else:
        raise FunctionError("Expected function get_prompts, but received other function")

# Send a GET request to an URL
def get_image(url):    
    response = requests.get(url)
    return response.content

# Save an image locally
def save_image(name, image):
    # Example name: "2024-08-18 09:53:18name.png"
    name = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + name + ".png"
    with open(name, "wb") as f:
        f.write(image)
    print(f"An image has been saved at {name}.")

# Request one or more images from DALL-E and save them locally    
def image_request(prompts):
    for prompt in prompts:
        urls =  query_dalle(prompt["content"])
        for url in urls:
            image = get_image(url)
            save_image(prompt["title"], image)