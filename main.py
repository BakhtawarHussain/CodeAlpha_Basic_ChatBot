def chat(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm fine, thanks! What about you?"
    elif "i'm fine" in user_input or "i am fine" in user_input:
        return "That's great to hear! What's your name?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {name}! What's your favorite color?"
    elif any(color in user_input for color in ["red", "blue", "green", "purple", "yellow", "black", "white"]):
        return "That's a beautiful color! What do you like to do in your free time?"
    elif any(activity in user_input for activity in ["reading", "drawing", "coding", "gaming", "watching movies", "writing"]):
        return "That sounds fun! How are you feeling today?"
    elif any(feeling in user_input for feeling in ["happy", "sad", "tired", "excited", "angry", "bored"]):
        return "Thanks for sharing! Is there anything you'd like to talk about?"
    elif "nothing" in user_input or "no" in user_input:
        return "Alright, feel free to chat anytime. 😊"
    else:
        return "I don't understand that. Can you tell me more?"
# Chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat(user_input)
    print("Chatbot:", response)