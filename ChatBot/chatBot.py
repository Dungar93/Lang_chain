import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import time

load_dotenv()

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "api_key" not in st.session_state:
    st.session_state.api_key = os.getenv("GOOGLE_API_KEY")

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "should_send" not in st.session_state:
    st.session_state.should_send = False

# Page Configuration
st.set_page_config(page_title="AI ChatBot", page_icon="robot", layout="wide")

# Custom CSS for better UI
st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        text-align: left;
    }
    .assistant-message {
        background-color: #f3e5f5;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

st.header("AI ChatBot Assistant")

# Sidebar Configuration
with st.sidebar:
    st.subheader("Settings")
    
    # Temperature Control
    temperature = st.slider(
        "Temperature (Creativity Level)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher = more creative, Lower = more focused"
    )
    
    # Clear Chat Button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")
    
    st.markdown("---")
    st.caption("Tips: Ask anything! The AI will help you.")

# Check if API key is set
if not st.session_state.api_key:
    st.error("GOOGLE_API_KEY not found in .env file. Please add it to use the chatbot.")
    st.stop()

# Initialize the model (only once, not on every rerun)
@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        google_api_key=st.session_state.api_key,
        timeout=30
    )

model = get_model()

# Display Chat History
st.subheader("Chat History")
chat_container = st.container()

with chat_container:
    for i, message in enumerate(st.session_state.chat_history):
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.write(message.content)

# Input Section
st.markdown("---")

# Callback function for Enter key
def on_enter_pressed():
    if st.session_state.user_input_field.strip():
        st.session_state.should_send = True

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "Ask me anything...", 
        placeholder="Type your question here... (Press Enter to send)",
        value=st.session_state.user_input,
        key="user_input_field",
        on_change=on_enter_pressed
    )

with col2:
    send_button = st.button("Send", use_container_width=True)

# Process user input
if (send_button or st.session_state.should_send) and user_input:
    # Reset flag
    st.session_state.should_send = False
    # Add user message to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    # Display user message immediately
    with chat_container:
        with st.chat_message("user"):
            st.write(user_input)
    
    # Clear the input field
    st.session_state.user_input = ""
    
    # Get AI response
    start_time = time.time()
    with st.spinner("⏳ Calling Gemini API... (This may take 3-8 seconds)"):
        try:
            # Build conversation messages
            messages = st.session_state.chat_history.copy()
            
            # Create model instance
            temp_model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=temperature,
                google_api_key=st.session_state.api_key,
                timeout=60
            )
            
            # Invoke the model
            response = temp_model.invoke(messages)
            ai_response = response.content
            
            # Calculate time taken
            elapsed = time.time() - start_time
            
            # Add AI message to history
            st.session_state.chat_history.append(AIMessage(content=ai_response))
            
            # Display AI response
            with chat_container:
                with st.chat_message("assistant"):
                    st.write(ai_response)
                    st.caption(f"⏱️ API Response time: {elapsed:.1f} seconds")
            
            # Rerun after displaying response to clear input
            st.rerun()
        
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.caption("Check: 1) Internet connection 2) API key valid 3) API quotas not exceeded")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 12px; color: gray;">
     Powered by Gemini AI | LangChain | Streamlit
    </div>
""", unsafe_allow_html=True)
