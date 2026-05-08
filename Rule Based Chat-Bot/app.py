from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')


def get_bot_response(user_input):
    """Rule-based chatbot logic."""
    user = user_input.lower().strip()

    if not user:
        return "Please type something so I can help you! 😊"

    # Exit Commands
    if user in ["exit", "bye", "quit", "goodbye"]:
        return "Thank you for visiting DecodeLabs. Goodbye 👋"

    # Greetings
    elif user in ["hi", "hello", "hey", "salam"]:
        return "Hello! Welcome to DecodeLabs AI Internship Program 🤖"

    # About DecodeLabs
    elif "decodelabs" in user or "decode labs" in user:
        return "DecodeLabs provides mentor-guided virtual internships, real projects, and career-ready skill development."

    # Internship Questions
    elif "internship" in user:
        return "DecodeLabs offers internships in AI, Python, Full Stack Development, Data Science, and more."

    # AI Internship
    elif "ai" in user or "artificial intelligence" in user:
        return "The AI internship teaches AI fundamentals, machine learning, logic building, and project development."

    # Skills
    elif "skills" in user:
        return "Important skills include Python, control flow, logic building, problem solving, and decision making."

    # Duration
    elif "duration" in user or "weeks" in user:
        return "The internship duration is approximately 4 weeks."

    # Mentorship
    elif "mentor" in user or "mentorship" in user:
        return "DecodeLabs provides mentor guidance and weekly checkpoints."

    # Certificate
    elif "certificate" in user:
        return "Students receive a verified certificate after successful completion of projects."

    # Careers
    elif "career" in user or "job" in user:
        return "DecodeLabs helps students build portfolio projects for better career opportunities."

    # Python
    elif "python" in user:
        return "Python is one of the main programming languages used in the internship projects."

    # Machine Learning
    elif "machine learning" in user:
        return "Machine Learning is a branch of AI where systems learn patterns from data."

    # Data Science
    elif "data science" in user:
        return "Data Science involves analyzing data and extracting useful insights."

    # Contact
    elif "contact" in user or "email" in user:
        return "You can contact DecodeLabs through their official website: www.decodelabs.tech"

    # Help
    elif "help" in user:
        return "You can ask me about internships, AI, Python, certificates, mentorship, and careers."

    # Default Response
    else:
        return "Sorry, I do not understand that question. Please ask something related to DecodeLabs or AI internship."


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/readme-preview')
def readme_preview():
    return send_from_directory('.', 'preview_readme.html')


@app.route('/README.md')
def readme_file():
    return send_from_directory('.', 'README.md')


@app.route('/screenshots/<path:filename>')
def screenshots(filename):
    return send_from_directory('screenshots', filename)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
