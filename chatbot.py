from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 😊 How can I help you?"

    elif "your name" in user_input:
        return "I am a web-based chatbot created for CODSOFT Task 1."

    elif "bye" in user_input:
        return "Goodbye! 👋"

    else:
        return "Sorry, I didn't understand that. Try again 🤔"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return jsonify({"response": chatbot_response(user_text)})

if __name__ == "__main__":
    app.run(debug=True)
