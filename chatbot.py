def chat_bot():
  print("SimpBot: Hello there! I am SimpBot, your AI chat_bot. Type something to chat with  me. Type 'exit' or 'bye' to end the chat.")
  
  while True:
    user_text=input("You: ").lower()
    
    if user_text in ["exit","bye"]:
      print("SimpBot: Goodbye! Have a great day!")
      break

    elif "hello" in user_text or "hi" in user_text:
      print("SimpBot: Hi! How can I assist you?")

    elif "how are you" in user_text:
      print("SimpBot: I am functioning perfectly. Thanks for asking! how are you?")

      user_response=input("You: ").lower()

      if ("not good" in user_response or "not well" in user_response or "bad" in user response):
        print("SimpBot: Sorry to hear that... Hope you feel goodsooner.")
        continue

      elif ("good" in user_response or "fine" in user_response):
        print("SimpBot: That's great!")
        continue

      else:
        print("SimpBot: Sorry I couldn't get that. Can you please type again?")
        continue

    elif "your name" in user_text:
      print("SimpBot: I'm SimpBot, your friendly Python Chatbot.")

    elif "help" in user_text or "what can you do" in user_text:
      print("SimpBot: I can respond to greetings, tell you my name, and say goodbye. Try typing something!")

    else:
      print("SimpBot: Hmm, I didn't quite get that. Could you try again?")

chat_bot()
      
      
