from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Setup the OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Format user content for API calls
def format_user_content(user_content):
    return {"role": "user",
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