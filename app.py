import streamlit as st
import uuid

from langchain_ollama import ChatOllama

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.chat_history import (
    InMemoryChatMessageHistory
)

from langchain_core.runnables.history import (
    RunnableWithMessageHistory
)


st.set_page_config(
    page_title="Local AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Local LLM Chatbot")
st.write("Chat with AI using LangChain Memory")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

@st.cache_resource
def create_chatbot():

    store = {}

    def get_session_history(session_id):

        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()

        return store[session_id]

    llm = ChatOllama(
        model="llama3.2",
        temperature=0.7
    )

    prompt = ChatPromptTemplate.from_messages([

        ("system", "You are a helpful AI assistant. "
         "Answer questions in simple English."),

        MessagesPlaceholder(variable_name="history"),

        ("human", "{question}")

    ])


    chain = prompt | llm

    chatbot = RunnableWithMessageHistory(

        chain,

        get_session_history,

        input_messages_key="question",

        history_messages_key="history"

    )

    return chatbot, store


chatbot, store = create_chatbot()

if st.button("Clear Chat"):

    store[st.session_state.session_id].clear()

    st.rerun()

history = store.get(
    st.session_state.session_id,
    InMemoryChatMessageHistory()
)

for message in history.messages:

    if message.type == "human":

        with st.chat_message("user"):
            st.write(message.content)

    elif message.type == "ai":

        with st.chat_message("assistant"):
            st.write(message.content)

user_input = st.chat_input("Type your message here...")


if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    try:

        with st.spinner("AI is thinking..."):

            response = chatbot.invoke(

                {"question": user_input},

                config={
                    "configurable": {
                        "session_id": st.session_state.session_id
                    }
                }

            )

        with st.chat_message("assistant"):
            st.write(response.content)

    except Exception as e:

        st.error(
            "Unable to connect to Ollama. "
            "Please check whether Ollama is running."
        )
