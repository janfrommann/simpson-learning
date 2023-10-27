import openai
import streamlit as st

# Sidebar for API key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

# Set the OpenAI API key
if openai_api_key:
    openai.api_key = openai_api_key

# Main page layout
st.title("💬 Talk to ChatGPT")
st.caption("This is a Chatbot based on OpenAI ChatGPT")

# Initialize messages if they don't exist in the session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display the chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Initialize 'user_input' to None to avoid NameError
user_input = None  # This line is crucial; it initializes 'user_input'

# Sidebar for predefined prompts and responses
with st.sidebar:
    st.header("Predefined Prompts")
    prompt_buttons = {
        "Explain Confounders": "What's the weather like today?",
        "Tell me about Spurious Correlations": "Tell me the latest news.",
        "How can I recognise Simpson's Paradox?": "Tell me a joke."
        # Add more buttons and prompts as needed
    }

    # Loop over the predefined prompts and create buttons for each in the sidebar
    for prompt in prompt_buttons:
        if st.button(prompt):
            user_input = prompt_buttons[prompt]  # Assigns new value if button is pressed

    st.header("Responses")
    response_buttons = {
        "Give more details": "Can you provide more details?",
        "Simplify your answer": "That seems complicated. Can you explain it in simpler terms?"
    }

    # Loop over the response prompts and create buttons for each in the sidebar
    for response in response_buttons:
        if st.button(response):
            user_input = response_buttons[response]  # Assigns new value if button is pressed

# Process the user input after checking if it's not None (meaning a button was pressed)
if user_input:  # This check is safe now as 'user_input' is defined in the scope
    # Add the user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get a response from the GPT-3 model
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
