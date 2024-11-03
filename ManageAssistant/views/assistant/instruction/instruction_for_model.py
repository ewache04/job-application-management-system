# ManageAssistant/instruction_for_model.py

def create_instruction(user_prompt):
    """
    Define the conversation messages for ChatGPT.

    Parameters:
        user_prompt (str): The user prompt for the conversation.

    Returns:
        list: A list of message diction
        aries representing the conversation.
    """
    return [
        {"role": "user", "content": "Hello! Could you please provide response to my prompt?"},
        {"role": "assistant", "content": "Certainly! Feel free to make a request."},
        {"role": "assistant", "content": "Great! How can I assist you further today?"},
        {"role": "user", "content": f" here is my prompt: {user_prompt}"},
    ]
