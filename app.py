# import streamlit as st
# from groq import Groq

# import json

# with open("dataset.json") as f:
#     data = json.load(f)

# for item in data:
#     print(item["question"], "->", item["answer"])

# client = Groq(api_key="api_key_here")

# with open("nana_personality.txt") as f:
#     personality = f.read()

# st.title("👴 Nana Ji AI Assistant")

# user_input = st.text_input("Talk to Nana Ji")

# if user_input:

#     prompt = personality + "\nUser: " + user_input

#     response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[{"role":"user","content":prompt}]
# )

#     answer = response.choices[0].message.content

#     st.write("👴 Nana Ji:", answer)


# import streamlit as st
# from groq import Groq
# import json
# # from voice import listen, speak
# import os

# ONLINE = os.getenv("STREAMLIT_SERVER_RUNNING", "false")

# # API


# import os
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# # Page settings
# st.set_page_config(page_title="Nana Ji AI", page_icon="👴", layout="centered")

# # Custom CSS
# st.markdown("""
# <style>
# .chat-user {
#     background-color: #d1e7ff;
#     padding: 10px;
#     border-radius: 10px;
#     margin-bottom: 10px;
# }
# .chat-ai {
#     background-color: #f4f4f4;
#     padding: 10px;
#     border-radius: 10px;
#     margin-bottom: 10px;
# }
# </style>
# """, unsafe_allow_html=True)

# # Title
# st.title("👴 Nana Ji AI Assistant")
# st.write("Talk to your wise Nana Ji for advice.")

# # Load personality
# with open("nana_personality.txt") as f:
#     personality = f.read()

# # Load dataset
# with open("dataset.json") as f:
#     dataset = json.load(f)

# examples = ""
# for item in dataset:
#     examples += f"User: {item['question']}\nNana Ji: {item['answer']}\n"

# # Chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # User input
# user_input = st.chat_input("Ask Nana Ji something...")

# if user_input:

#     # Show user message
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     prompt = personality + "\n\nExamples:\n" + examples + "\nUser: " + user_input

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role":"user","content":prompt}]
#     )

#     answer = response.choices[0].message.content

#     st.session_state.messages.append({"role": "ai", "content": answer})

# # Display chat
# for msg in st.session_state.messages:
#     if msg["role"] == "user":
#         st.markdown(f'<div class="chat-user">🧑‍💻 <b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="chat-ai">👴 <b>Nana Ji:</b> {msg["content"]}</div>', unsafe_allow_html=True)

# # Sidebar
# st.sidebar.title("About Nana Ji AI")
# st.sidebar.write("""
# 👴 **Nana Ji AI Assistant**

# A personality-based AI chatbot that gives
# life advice like a wise Indian grandfather.

# Built using:
# - Python
# - Streamlit
# - Groq API
# """)

# #Voice Button
# # if st.button("🎤 Talk to Nana Ji"):
# #     user_input = listen()

# # if user_input:

# #     response = client.chat.completions.create(
# #         model="llama-3.3-70b-versatile",
# #         messages=[
# #             {"role": "system", "content": "You are a wise Indian grandfather (Nana Ji) who gives life advice in simple Hindi."},
# #             {"role": "user", "content": user_input}
# #         ]
# #     )

# #     answer = response.choices[0].message.content

# #     st.write("👴 Nana Ji:", answer)

# #     speak(answer)

# ##################################
# # if st.button("🎤 Talk to Nana Ji"):

# #     user_input = listen()

# #     if user_input:

# #         st.write("You:", user_input)

# #         response = client.chat.completions.create(
# #             model="llama-3.3-70b-versatile",
# #             messages=[{"role":"user","content":user_input}]
# #         )

# #         answer = response.choices[0].message.content

# #         st.write("👴 Nana Ji:", answer)

# #         speak(answer)

# import streamlit as st
# from voice import listen, speak

# if st.button("🎤 Talk to Nana Ji"):

#     st.write("🎤 Listening... Please speak")

#     user_input = listen()

#     if user_input:
#         st.write("You:", user_input)

#         answer = "Beta mehnat karo aur chinta mat karo."   # temporary test response

#         st.write("👴 Nana Ji:", answer)

#         # speak(answer)   # disabled for cloud deployment

#     else:
#         st.write("⚠️ Could not hear you. Please try again.")


# # from dotenv import load_dotenv
# # load_dotenv()

# ################3
# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))


import streamlit as st
from groq import Groq
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page settings
st.set_page_config(page_title="Nana Ji AI", page_icon="👴", layout="centered")

# Custom CSS
st.markdown("""
<style>
.chat-user {
    background-color: #d1e7ff;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.chat-ai {
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("👴 Nana Ji AI Assistant")
st.write("Talk to your wise Nana Ji for advice.")

# Load personality
with open("nana_personality.txt") as f:
    personality = f.read()

# Load dataset
with open("dataset.json") as f:
    dataset = json.load(f)

examples = ""
for item in dataset:
    examples += f"User: {item['question']}\nNana Ji: {item['answer']}\n"

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Ask Nana Ji something...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    prompt = personality + "\n\nExamples:\n" + examples + "\nUser: " + user_input

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}]
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append({"role": "ai", "content": answer})

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="chat-user">🧑‍💻 <b>You:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="chat-ai">👴 <b>Nana Ji:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )

# Sidebar
st.sidebar.title("About Nana Ji AI")

st.sidebar.write("""
👴 **Nana Ji AI Assistant**

A personality-based AI chatbot that gives life advice like a wise Indian grandfather.

Built using:
- Python
- Streamlit
- Groq API
""")