import streamlit as st
from AI import generate_response
from langchain.prompts import ChatPromptTemplate
if "messages" not in st.session_state.keys():

    st.session_state.messages=[
        {"role":"assistant","content":"Hey there Weather man here,How can i help you?"}

    ]
#display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


#get user inputs 
prompt=st.chat_input()

if prompt is not None:

    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
# Define the chat prompt template
prompt_template = ChatPromptTemplate.from_template(
    '''
    You are a very friendly and charming AI assistant. Help answer the user's questions in a friendly and funny tone. Your responses should be in the language specified. Demonstrate this in your response.
    Human: {question}
    '''
)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            prompt=prompt_template.format(question=prompt)
            ai_response=generate_response(prompt)
            print(ai_response)
            st.write(ai_response)
            

    new_ai_message = {"role": "user", "content": ai_response}
    st.session_state.messages.append(new_ai_message)
    




