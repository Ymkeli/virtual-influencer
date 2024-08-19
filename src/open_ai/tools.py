dalle_prompts = {
    "type": "function",
    "function": {
        "name": "get_prompts",
        "description": "Returns multiple prompts for DALL·E based on an Instagram post.",
        "parameters": {
            "type": "object",
            "properties": {
                "prompts": {
                    "type": "array",
                    "description": "An array of objects, where each object contains a title and a prompt.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the prompt."
                                },
                            "content": {
                                "type": "string",
                                "description": "The prompt associated with the title."
                                }
                            },
                        "required": ["title", "prompt"]
                        }
                    }
                },
            "required": ["prompts"]
            }
        }
    }