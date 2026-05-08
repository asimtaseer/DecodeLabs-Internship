# DecodeLabs Rule-Based AI Chatbot

print("=" * 60)
print("      Welcome to DecodeLabs AI Chatbot 🤖")
print("=" * 60)
print("Type 'exit' anytime to close the chatbot.\n")

while True:

    user = input("You: ").lower()

    # Exit Commands
    if user in ["exit", "bye", "quit", "goodbye"]:
        print("Bot: Thank you for visiting DecodeLabs. Goodbye 👋")
        break

    # Greetings
    elif user in ["hi", "hello", "hey", "salam"]:
        print("Bot: Hello! Welcome to DecodeLabs AI Internship Program 🤖")

    # About DecodeLabs
    elif "decodelabs" in user or "decode labs" in user:
        print("Bot: DecodeLabs provides mentor-guided virtual internships, real projects, and career-ready skill development.")

    # Internship Questions
    elif "internship" in user:
        print("Bot: DecodeLabs offers internships in AI, Python, Full Stack Development, Data Science, and more.")

    # AI Internship
    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: The AI internship teaches AI fundamentals, machine learning, logic building, and project development.")


    # Skills
    elif "skills" in user:
        print("Bot: Important skills include Python, control flow, logic building, problem solving, and decision making.")

    # Duration
    elif "duration" in user or "weeks" in user:
        print("Bot: The internship duration is approximately 4 weeks.")

    # Mentorship
    elif "mentor" in user or "mentorship" in user:
        print("Bot: DecodeLabs provides mentor guidance and weekly checkpoints.")

    # Certificate
    elif "certificate" in user:
        print("Bot: Students receive a verified certificate after successful completion of projects.")

    # Careers
    elif "career" in user or "job" in user:
        print("Bot: DecodeLabs helps students build portfolio projects for better career opportunities.")

    # Python
    elif "python" in user:
        print("Bot: Python is one of the main programming languages used in the internship projects.")

    # Machine Learning
    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI where systems learn patterns from data.")

    # Data Science
    elif "data science" in user:
        print("Bot: Data Science involves analyzing data and extracting useful insights.")

    # Contact
    elif "contact" in user or "email" in user:
        print("Bot: You can contact DecodeLabs through their official website: www.decodelabs.tech")

    # Help
    elif "help" in user:
        print("Bot: You can ask me about internships, AI, Python, Project 1, certificates, mentorship, and careers.")

    # Default Response
    else:
        print("Bot: Sorry, I do not understand that question. Please ask something related to DecodeLabs or AI internship.")