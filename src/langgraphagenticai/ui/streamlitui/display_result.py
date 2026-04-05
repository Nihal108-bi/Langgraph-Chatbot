import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        # Improved handling for Basic Chatbot streaming
        if self.usecase == "Basic Chatbot":
            for event in self.graph.stream({'messages': ("user", self.user_message)}):
                for value in event.values():
                    msg = value['messages']
                    if isinstance(msg, AIMessage) and msg.content:
                        with st.chat_message("assistant"):
                            st.write(msg.content)

        # Functional logic for Chatbot with Web
        elif self.usecase == "Chatbot with Web":
            initial_state = {"messages": [HumanMessage(content=self.user_message)]}
            # graph.invoke will now run the chatbot -> tools -> chatbot cycle
            res = self.graph.invoke(initial_state)
            
            for message in res['messages']:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)
                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
                elif isinstance(message, ToolMessage):
                    with st.expander("🛠️ Tool Output (Web Search)"):
                        st.write(message.content)                        

        elif self.usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = self.graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")