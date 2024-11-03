# openai_tools/response_generator.py
from general_utils.get_horizontal_line import get_horizontal_line
from openai_tools.openai_custom_settings.settings import get_assistant_settings


def format_instruction_for_model(value):
    return value


def generate_response(user_prompt, client=None, model=None,
                      temperature=None, max_tokens=None, top_p=None,
                      frequency_penalty=None, presence_penalty=None):

    if client:

        # Fetch AssistantSettings from the database
        settings = get_assistant_settings()

        instruction_to_openai = format_instruction_for_model(user_prompt)

        if not settings:
            # Handle case where settings are not available
            return None

        # Extract settings from the AssistantSettings instance
        model = settings.get('selected_model') or model
        # print(f'model: {model}')

        temperature = settings.get('temperature') or temperature
        # print(f'temperature: {temperature}')

        max_tokens = max_tokens or settings.get('max_tokens')
        # print(f'max_tokens: {max_tokens}')

        top_p = top_p or settings.get('top_p')
        # print(f'top_p: {top_p}')

        frequency_penalty = frequency_penalty or settings.get('frequency_penalty')
        # print(f'frequency_penalty: {frequency_penalty}')

        presence_penalty = presence_penalty or settings.get('presence_penalty')
        # print(f'presence_penalty: {presence_penalty}')

        # Generate response using the OpenAI API
        response = client.chat.completions.create(
            model=model,
            messages=instruction_to_openai,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )

        print(get_horizontal_line())

        return response.choices[0].message.content
    else:
        # Handle case where client is not available
        return None
