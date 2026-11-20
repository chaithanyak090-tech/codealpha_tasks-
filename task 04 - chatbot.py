
# Basic Rule-Based Chatbot

# Function to generate chatbot responses
def chatbot_response(user_message):

    user_message = user_message.lower().strip()

    if user_message == "hello" or user_message == "hi":
        return "Hello! Welcome. How can I help you?"

    elif user_message == "how are you":
        return "I'm fine, thanks for asking!"

    elif user_message == "what is your name":
        return "I'm Python Chatbot."

    elif user_message == "what can you do":
        return "I can chat with you and answer simple messages."

    elif user_message == "thank you":
        return "You're welcome!"

    elif user_message == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that message."


# Main chatbot program

print("       PYTHON CHATBOT        ")


print("Chatbot: Hello! Type 'bye' to exit.")

while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if user_input.lower().strip() == "bye":
        break
