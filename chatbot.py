def chatbot_response(user_input):

    user_input = user_input.lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input:
        return "Hello! 😊 How can I help you today?"

    # Name
    elif "your name" in user_input:
        return "I'm a chatbot created for CODSOFT Internship Task 1."

    # Asking how bot is
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! 🤖"

    # AI related
    elif "what is ai" in user_input or "artificial intelligence" in user_input:
        return "AI means Artificial Intelligence, where machines can think and make decisions like humans."

    # Creator information
    elif "who created you" in user_input:
        return "I was created by Niranjana as part of the CODSOFT AI internship."

    # Goodbye
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Have a great day!"

    # Default fallback
    else:
        return "Sorry, I didn't understand that. ❓ Try asking something else!"


print("🤖 CODSOFT AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_text = input("You: ")
    bot_reply = chatbot_response(user_text)
    print("Bot:", bot_reply)

    if "bye" in user_text.lower():
        break
