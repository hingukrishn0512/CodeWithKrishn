
import re

# A dictionary to store questions and their corresponding answers
responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great, thank you for asking!",
    "what is your name": "I'm an AI chatbot, created to assist you.",
    "bye": "Goodbye! Have a great day!",
}

# Function to handle user input and return the appropriate response
def chatbot_response(user_input):
    # Convert user input to lowercase for pattern matching
    user_input = user_input.lower()

    # Look for an exact match in the responses dictionary
    for pattern, response in responses.items():
        if re.search(r'\b' + re.escape(pattern) + r'\b', user_input):  # Match whole words only
            return response
    
    # If no match is found, return a default response
    return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Function to start the chat with the bot
def chat_with_bot():
    print("Hello! I am your chatbot. Type 'bye' to exit the conversation.")
    
    while True:
        # Take user input
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Goodbye!")
            break
        
        # Get the response from the chatbot
        response = chatbot_response(user_input)
        print(f"AIChatBot: {response}")

if __name__ == "__main__":
    chat_with_bot()
