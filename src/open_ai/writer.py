from open_ai.request import format_content, query_open_ai

# writer prompt
writer_prompt = {"role": "system", "content": "You are a writer for a travel influencer. You write stories about imagenary worlds on far away planets."}

def writer_request(user_content):
    messages = [writer_prompt,
                format_content("user", user_content)]
    response = query_open_ai(messages)
    system_message = format_content("system", response)
    messages.append(system_message)
    return {"content": response, 
            "messages": messages}
                