while True:
    message = input("You: ")

    if message.lower() == "hello":
        print("Bot: Hi!")
    elif message.lower() == "how are you":
        print("Bot: I am fine.")
    elif message.lower() == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")