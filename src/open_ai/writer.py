from open_ai.request import format_user_content, query_open_ai

# writer prompt
writer_prompt = {"role": "system", "content": "You are a writer for a travel influencer. You write stories about imagenary worlds on far away planets."}

def writer_request(user_content):
    messages = [writer_prompt,
                format_user_content(user_content)]
    response = query_open_ai(messages)
    return response
                