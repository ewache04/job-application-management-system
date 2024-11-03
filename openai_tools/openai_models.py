# openai_tools/openai_models.py
from openai_tools.open_model_group.DALL_E_category import dall_e_category
from openai_tools.open_model_group.Embeddings_category import embeddings_category
from openai_tools.open_model_group.GPT_3_category import gpt_3_category
from openai_tools.open_model_group.GPT_4_category import gpt_4_category
from openai_tools.open_model_group.Moderation_category import moderation_category
from openai_tools.open_model_group.TTS_category import tts_category
from openai_tools.open_model_group.Whisper_category import whisper_category


def get_openai_models():

    combined_categories = (
        gpt_3_category()
        # gpt_4_category() +
        # dall_e_category() +
        # tts_category() +
        # whisper_category() +
        # embeddings_category() +
        # moderation_category()
    )

    return combined_categories


# Test the function
# combined_categories = get_openai_models()
# print(combined_categories)

