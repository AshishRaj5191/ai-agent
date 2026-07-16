import streamlit as st
from agent import Agent

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.stChatMessage{
    border-radius:12px;
    padding:10px;
}

h1{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Agent")
st.caption("Powered by Groq + Llama 3.3")

# -----------------------------
# Agent
# -----------------------------
if "agent" not in st.session_state:
    st.session_state.agent = Agent()

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("⚙ Controls")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.write("### Features")
    st.write("✅ Conversation Memory")
    st.write("✅ Calculator Tool")
    st.write("✅ Groq Llama 3.3")

# -----------------------------
# Show Chat History
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
prompt = st.chat_input("Ask something...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = st.session_state.agent.run(prompt)

            except Exception as e:
                response = f"❌ Error:\n\n{e}"

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )