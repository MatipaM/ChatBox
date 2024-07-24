from API import API
from Conversation import Conversation
from MessageFactory import MessageFactory

import streamlit as st

class Interface():
    response = ""
    
    question = API.get_instance().query_ai("interesting questions")
    suggestions = (question['response'])
    suggestion = suggestions[suggestions.index("2.")+3:suggestions.index("3.")]
    inputBox = st.text_input("Message AI") #in second quoatations, put AI suggestions
    st.write(f"Suggestion: {suggestion}")

    def createConvo(inputBox, response, ai_type):
        conversations = [MessageFactory.createMessage('user',inputBox), MessageFactory.createMessage(ai_type, response['response'])]
        for chat in conversations:
            print("chat", chat)
            Conversation.get_instance().add(chat)

        Conversation.get_instance().update()
        st.write(response['response'])

    if st.button("Ask Friendly"):
        response = API.get_instance().query_ai(f"write a friendly response to: {inputBox}")
        createConvo(inputBox, response, 'friendly_ai')
    elif st.button("Ask Sophisticated"):
        response = API.get_instance().query_ai(f"write a sophisticated response to: {inputBox}")
        createConvo(inputBox, response, 'sophisticated_ai')
    elif st.button("Ask Normal"):
        response = API.get_instance().query_ai(inputBox)
        createConvo(inputBox, response, 'ai')


        



    
    
