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
    option = st.selectbox(
     'Select which AI you would like to use',
     ('friendly_ai', 'sophisticated_ai', 'ai'))

    st.write('You selected:', option)

    def createConvo(inputBox, response, ai_type):
        conversations = [MessageFactory.createMessage('user',inputBox), MessageFactory.createMessage(ai_type, response['response'])]
        for chat in conversations:
            print("chat", chat)
            Conversation.get_instance().add(chat)

        Conversation.get_instance().update()
        st.write(response['response'])

    if st.button("Ask"):
        response = API.get_instance().query_ai(f"write a {option} response to: {inputBox}")
        createConvo(inputBox, response, option)


    


        



    
    
