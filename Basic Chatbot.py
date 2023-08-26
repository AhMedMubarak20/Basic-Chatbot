def chatbot():
    print("Chatbot: Hi there! I'm a basic chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm still learning. Can you be more specific?")

chatbot()
