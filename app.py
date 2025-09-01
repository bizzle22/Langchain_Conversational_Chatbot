import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")

# --- App Structure ---
st.set_page_config(page_title="Conversational Chatbot")
st.header("Gemini Conversational Chatbot 🚀")

# Check for API key
if not google_api_key:
    st.error("Google API key is not set! Please add it to your .env file.")
else:
    # --- Model Loading ---
    @st.cache_resource
    def load_llm():
        """Loads the Gemini model."""
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
        return llm

    llm = load_llm()

    # --- Session State Initialization ---
    # Initialize chat history if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # --- Display Chat History ---
    # Display previous messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message.type):
            st.markdown(message.content)

    # --- User Input and Chat Logic ---
    # Get user input from the chat input box
    if prompt := st.chat_input("What is up?"):
        # Add user message to session state and display it
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("human"):
            st.markdown(prompt)

        # Get AI response
        with st.spinner("Thinking..."):
            # The LLM now receives the whole history
            response = llm.invoke(st.session_state.messages)

        # Add AI response to session state and display it
        st.session_state.messages.append(AIMessage(content=response.content))
        with st.chat_message("ai"):
            st.markdown(response.content)