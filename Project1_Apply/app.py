def standrize(text:str):
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return " ".join(text.split())


intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hi there! How can I help you today?",
    },
    "how_are_you": {
        "patterns": ["how are you", "how are you doing", "whats up"],
        "response": "I'm running at 100% logic. How about you?",
    },
    "name": {
        "patterns": ["what is your name", "who are you", "your name"],
        "response": "I'm a rule-based chatbot built at DecodeLabs.",
    },
    "capabilities": {
        "patterns": ["help", "what can you do"],
        "response": "I can handle greetings, answer a few questions, and say goodbye. Type 'exit' to quit.",
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx"],
        "response": "You're welcome!",
    },
    "creator": {
        "patterns": ["who made you", "who created you"],
        "response": "A student engineer, using nothing but control flow and a dictionary.",
    },
}

LOOKUP = {
    standrize(p): data["response"]
    for data in intents.values()
    for p in data["patterns"]
}


EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}
FALLBACK = "I do not understand. Try 'help' to see what I can do."



def chat_bot():
    print("Bot: Hello! Type 'help' for options or 'exit' to quit.")
    while True:
        try:
            raw = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Session terminated. Goodbye!")
            break

        clean = standrize(raw)

        if not clean:
            print("Bot: Say something and I'll respond.")
            continue
        elif clean in EXIT_COMMANDS:
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print(f"Bot: {LOOKUP.get(clean, FALLBACK)}")

chat_bot()
