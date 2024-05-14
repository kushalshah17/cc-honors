import nltk
import re

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Department information
departments = {
    'extc': {
        'name': 'Electronics and Telecommunication',
        'seats': 80,
        'eligibility': 'Minimum 50% in 12th standard with Mathematics.'
    },
    'it': {
        'name': 'Information Technology',
        'seats': 70,
        'eligibility': 'Minimum 50% in 12th standard with Mathematics.'
    },
    'mech': {
        'name': 'Mechanical Engineering',
        'seats': 60,
        'eligibility': 'Minimum 50% in 12th standard with Physics and Mathematics.'
    },
    'cs': {
        'name': 'Computer Science',
        'seats': 70,
        'eligibility': 'Minimum 50% in 12th standard with Mathematics.'
    }
}

# Function to respond to user queries
def chatbot():
    print("Welcome to College Inquiry Chatbot!")
    name = input("May I know your name? ")
    print(f"Hello {name}!")

    while True:
        print("\nWhat information do you need? You can ask about departments, seats, or eligibility.")
        query = input("> ").lower()

        # Department information
        if re.search(r'\b(departments)\b', query):
            print("Available departments are:")
            for key, value in departments.items():
                print(f"- {value['name']}")

        # Seats information
        elif re.search(r'\b(seats)\b', query):
            print("Seats available in each department:")
            for key, value in departments.items():
                print(f"- {value['name']}: {value['seats']} seats")

        # Eligibility information
        elif re.search(r'\b(eligibility)\b', query):
            print("Eligibility criteria for each department:")
            for key, value in departments.items():
                print(f"- {value['name']}: {value['eligibility']}")

        # End the conversation
        elif re.search(r'\b(exit|quit)\b', query):
            print("Thank you for using College Inquiry Chatbot. Goodbye!")
            break

        # Default response for unrecognized queries
        else:
            print("I'm sorry, I didn't understand that.")

# Run the chatbot
chatbot()
