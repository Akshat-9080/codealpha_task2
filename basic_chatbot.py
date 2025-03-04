#This is my second task of basic chatbot during my internship at code alpha.
import random

# Dictionary to hold questions and corresponding bot responses
response_dict = {
    "hello": ["Hi!", "Hello there!", "Hey! How can I assist you?"],
    "how are you": ["I'm doing well, thanks!", "I don't have feelings, but I'm functioning fine!"],
    "your name": ["I'm ChatBot, your assistant.", "I don't have a name, but you can call me ChatBot!"],
    "bye": ["Goodbye! Take care!", "Bye! See you soon!"],
    "default": ["I didn't quite understand that. Can you rephrase?", "Sorry, I can't get that."]
}

# Function to find and return the appropriate response
def generate_response(user_message):
    user_message = user_message.lower()  # Make the input lowercase for easy comparison
    
    # Loop through the dictionary and return the response if the user input matches
    for key in response_dict:
        if key in user_message:
            return random.choice(response_dict[key])
    
    # If no match found, return a default response
    return random.choice(response_dict["default"])

# Function to initiate the conversation and
