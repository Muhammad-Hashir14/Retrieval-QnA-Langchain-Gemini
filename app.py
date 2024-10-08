import streamlit as st
import os
from langchainhelper import createEmbeddings
from langchainhelper import createVectorDB
from langchainhelper import get_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Code Basics FAQs Bot", page_icon="🤖", layout="wide")

api_key = st.secrets["api_keys"]["API_KEY"]
os.environ["GOOGLE_API_KEY"] = api_key

llm = ChatGoogleGenerativeAI(model = "gemini-pro")
createVectorDB("FAISS")

st.title("Code Basics FAQs Bot 🤖")

with st.sidebar:
    st.header("Chat History")
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    for i, chat in enumerate(reversed(st.session_state.history)):
        if len(chat) == 2:  # Ensure each entry has exactly two items
            user_input, bot_response = chat
            st.write(f"Q{i + 1}: {user_input}")
            st.write(f"A{i + 1}: {bot_response}")
            st.write("--------------------------------")

st.text("Ask me anything about CodeBasics..")
user_input = st.text_input("Type your Question here ....", key = "user_input")

if user_input:
    chain = get_qa_chain("FAISS", llm)
    bot_response = chain.invoke(user_input)

    if isinstance(bot_response, str):
        st.session_state.history.append((user_input, f"Bot: {bot_response}"))
    else:
        st.session_state.history.append((user_input, f"Bot: {bot_response.get('result', "No result")}"))

st.write("### Chat")
for chat in reversed(st.session_state.history):
    if len(chat) == 2:  # Ensure there are exactly two items
        user_input, bot_response = chat
        with st.container():  # Create a container for each message
            st.markdown(f"""
            <div style="padding: 10px; margin: 10px 0; border-radius: 5px; background-color: #262730;">
                <strong>User:</strong> {user_input}<br>
                <strong>Bot:</strong> {bot_response}
            </div>
            """, unsafe_allow_html=True)