print("🤖 AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: I am an AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created by Nisha Singh.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
