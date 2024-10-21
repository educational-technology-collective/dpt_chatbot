from openai import OpenAI
import streamlit as st

st.title("Chat with John W or Senior PT")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def load_persona(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Load personas for patient and PT
patient_persona = load_persona('personas/patient_1.txt')
pt_persona = load_persona('personas/senior_pt.txt')

agent = st.selectbox("Who do you want to talk to?", ("John W (Patient)", "Senior PT"))

# Initialize session state for model and messages if not already present
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Displays the conversation history
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

persona = patient_persona if agent == "John W (Patient)" else pt_persona

#  Initialize the conversation with the current persona
if not st.session_state.messages:
    st.session_state.messages.append({"role": "system", "content": persona})


# This block handles the actual conversation
if prompt := st.chat_input("Ask a question:"):
    # Add user input to the conversation history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    stream = client.chat.completions.create(
        model=st.session_state["openai_model"],
        messages=[
            {"role": m["role"], "content": m["content"]} 
            for m in st.session_state.messages
        ],
        stream=True,
    )
    with st.chat_message("assistant"):
        response = st.write_stream(stream)

    # Add assistant response to conversation history
    st.session_state.messages.append({"role": "assistant", "content": response})
