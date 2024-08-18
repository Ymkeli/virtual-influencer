from open_ai.request import query_open_ai, query_dalle, format_content
from datetime import datetime
import requests

# Request a compact prompt for DALLE based on the generated post
def image_prompt_request(messages):
    user_content = format_content("user", 
                                  "Can you return a prompt for DALLE based on this instagram post? Keep it short and compact.")
    messages.append(user_content)
    response = query_open_ai(messages)
    return {"content": response, 
            "messages": messages}

# Send a GET request to an URL
def get_image(url):    
    response = requests.get(url)
    return response.content

# Save an image locally
def save_image(image):
    # Example name: "2024-08-18 09:53:18.png"
    name = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".png"
    with open(name, "wb") as f:
        f.write(image)
    print(f"An image has been saved at {name}.")

# Request one or more images from DALLE and save them locally    
def image_request(prompt):
    urls =  query_dalle(prompt)
    for url in urls:
        image = get_image(url)
        save_image(image)