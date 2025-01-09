import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Define intents and responses
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "take care"],
    "how_are_you": ["how are you", "how's it going", "how are you doing"],
}

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "how_are_you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine, thanks for asking."],
    "default": ["I'm sorry, I didn't understand that.", "Can you rephrase that?"]
}

# Preprocess user input
def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())  # Tokenize and lowercase
    filtered_tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    return filtered_tokens

# Match user input to an intent
def detect_intent(user_input):
    tokens = preprocess_input(user_input)
    for intent, keywords in intents.items():
        if any(keyword in tokens for keyword in keywords):
            return intent
    return "default"

# Get a response from the chatbot
def chatbot_response(user_input):
    intent = detect_intent(user_input)
    return random.choice(responses[intent])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
