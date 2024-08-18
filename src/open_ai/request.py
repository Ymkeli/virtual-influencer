from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Setup the OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Format user content for API calls
def format_content(role, user_content):
    return {"role": role,
            "content": user_content}
    
# Basic openAI API request.
def query_open_ai(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=300,
        temperature=1
    )
    return response.choices[0].message.content

# Basic request to DALL-E
def query_dalle(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        n=1,
        size="256x256")
    urls = [item.url for item in response.data]
    return urls