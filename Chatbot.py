import openai
import streamlit as st

# Custom CSS for the grayscale theme and subdued yellow buttons
st.markdown("""
    <style>
        body {
            color: #686868;
            background-color: #F5F5F5;
        }
        .stButton>button {
            background-color: #FAD02E;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Marcus AI-reulus")
st.caption("An AI-powered chatbot of the world's most famous philosopher-king")

# Placing the image in the center of the screen
st.image("https://i.imgur.com/aHhvLJm.png", use_column_width=True)

# Check if messages are not in session state
# If not, initialize with system message and assistant greeting
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are an AI modeled after Marcus Aurelius. Respond as he would, drawing from his philosophy and writings."},
        {"role": "assistant", "content": "How can I help you?"}
    ]

# Display the chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Check for user input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Placeholder sound while LLM is generating its response
    sound_placeholder = "https://path_to_your_sound_file.mp3"
    st.audio(sound_placeholder, format='audio/mp3')
    
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
