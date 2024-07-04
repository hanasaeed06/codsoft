import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I'm a chatbot created to help you with your queries."
    elif "help" in user_input:
        return "Sure! I'm here to help. Please ask your question."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what is your favorite color" in user_input:
        return "I like all colors, but I think blue is quite calming."
    elif "who created you" in user_input:
        return "I was created by a programmer using Python."
    elif "what can you do" in user_input:
        return "I can chat with you, answer simple questions, and keep you company!"
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "what is the capital of telangana" in user_input:
        return "The capital of Telangana is Hyderabad."
    elif "do you like music" in user_input:
        return "I'm a bot, so I don't listen to music, but I hear it's very enjoyable!"
    elif "what is the time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"

def chat():
    print("\033[92m" + """
*****************************************************
*                                                   *
*        Welcome to the Chatbot!                    *
*        Type 'bye' to exit.                        *
*                                                   *
*****************************************************
""" + "\033[0m")
    
    while True:
        try:
            user_input = input("\033[94m" + "You: " + "\033[0m")
            response = chatbot_response(user_input)
            print("\033[95m" + "Chatbot: " + "\033[0m" + "\033[93m" + response + "\033[0m")
            if user_input.lower() in ["bye", "goodbye"]:
                print("\033[92m" + """
*****************************************************
*                                                   *
*        Thank you for chatting!                    *
*        Have a great day!                          *
*                                                   *
*****************************************************
""" + "\033[0m")
                break
        except Exception as e:
            print("\033[91m" + f"An error occurred: {e}" + "\033[0m")

chat()
