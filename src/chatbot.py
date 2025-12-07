# src/chatbot.py
from rules import make_rules
from utils import log_message

def find_response(text, rules):
    for r in rules:
        m = r.match(text)
        if m:
            return r.render(m), r.name
    return ("Sorry, I didn't understand that.", "fallback")

def main():
    rules = make_rules()
    print("Task 1 Chatbot Started (type 'exit' to quit)")

    while True:
        user = input("You: ").strip()
        log_message("USER", user)

        if user.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            log_message("BOT", "Goodbye!")
            break

        resp, rule = find_response(user, rules)
        print("Bot:", resp)
        log_message("BOT", resp)

if __name__ == "__main__":
    main()
