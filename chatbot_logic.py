import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Basic keyword-based responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm doing fine!",
    "help": "Sure! Ask me anything.",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm not sure how to respond to that."
