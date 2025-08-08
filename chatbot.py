import random
import re
class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Greetings!"],
            "how are you": ["Doing well, how about you?"],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "default": ["I didn't understand that.", "Can you rephrase?", "Let's talk about something else."],
            #-- Add more responses as needed--
            "help me": ["Sure, what do you need help with?", "How can I assist you?"],
            "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
            "what is your name": ["I am a simple chatbot.", "Just a bot here to chat!"],
            "My name is (.*)": ["Nice to meet you, {}!", "Hello, {}! How can I assist you today?"],
            "what is my name": ["You told me your name is {}.", "I remember you said your name is {}."],
            "what can you do": ["I can chat with you, answer questions, and provide information."],

        }
        self.name = "Simple Chatbot"
        self.name_pattern = re.compile(r"My name is (.*)", re.IGNORECASE)
        self.user_name = None

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Check if the user input matches the name pattern
        name_match = self.name_pattern.match(user_input)
        if name_match:
            self.user_name = name_match.group(1).strip()
            return random.choice(self.responses["My name is (.*)"]).format(self.user_name)
        for key in self.responses:
            if re.search(r'\b' + re.escape(key) + r'\b', user_input):
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])
    
# Main loop to interact with the chatbot
def start(self):
    print("Simple Chatbot: Hello! How can I help you today?")
    # your loop to handle user input and chatbot responses

    current_topic = None #track the current topic of conversation

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input: # Handle empty input
                print("Simple Chatbot: I didn't catch that. Could you please say something?")
                continue
            # Check for exit commands
            if user_input.lower() in ["goodbye", "quit", "bye" , "exit"]:
                print("Simple Chatbot: Goodbye! It was nice talking to you!")
                break
            # Handle special cases
            if user_input.lower() == "menu":
                print("Simple Chatbot: Here are the available commands:")
                print("Simple Chatbot 'Menu' to see the list of commands.")
                print("Simple Chatbot 'history': View our conversation history.")
                print("Simple Chatbot 'reset': Start a new conversation.")
                print("Simple Chatbot 'thanks' to express gratitude.")
                print("Simple Chatbot: 'Bye' to exit the chat.")
                current_topic = "menu"

                continue
            
            elif user_input.lower() == "history":
                print("Simple Chatbot: Here is the conversation history:")
                # This would normally display the conversation history, but for simplicity, we just print a message.
                current_topic = "history"
                continue
            elif user_input.lower() == "reset":
                print("Simple Chatbot: Starting a new conversation. How can I help you today?")
                self.user_name = None
                current_topic = "reset"
                continue

            # Get response from the chatbot
            response = self.get_response(user_input)
            print(f"Simple Chatbot: {response}")
        except KeyboardInterrupt:
            print("\nSimple Chatbot: Goodbye! It was nice talking to you!")
            break
        except Exception as e: 
            print(f"An error occurred: {e}")
            break
            
if __name__ == "__start__":
    chatbot = SimpleChatbot()
    chatbot.start()  # Start the chatbot interaction loop
        







            