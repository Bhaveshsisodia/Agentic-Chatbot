import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage , ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self,usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if "messages" not in st.session_state:
            
            st.session_state["messages"] = []

        # print(usecase, graph , user_message)
        if usecase == "Basic Chatbot":


            # 2. First, display all previous messages (history)
            for msg in st.session_state["messages"]:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

            # 3. If there is no new user message this run, just stop here
            if not user_message:
                return

            # 4. Show current user message immediately
            with st.chat_message("user"):
                st.write(user_message)
            st.session_state["messages"].append({"role": "user", "content": user_message})

            # 5. Stream assistant reply and show it
            full_reply = ""  # will store the final assistant text

            with st.chat_message("assistant"):
                placeholder = st.empty()  # we update this as we stream

                for event in graph.stream({"messages": [HumanMessage(content=user_message)]}):
                    for value in event.values():
                        # You may need to adjust depending on how graph.stream emits messages
                        reply_text = value["messages"].content
                        full_reply = reply_text  # if last one is the final answer
                        placeholder.write(reply_text)

            # 6. Save assistant reply to history
            st.session_state["messages"].append(
                {"role": "assistant", "content": full_reply}
            )

        elif usecase == "Chatbot with Web":

            initial_messages = [HumanMessage(content=user_message)]
            res = graph.invoke({"messages": initial_messages})
            for message in res['messages']:
                if type(message)== HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing AI news..."):

                result = graph.invoke({"messages": frequency})
                try:
                    ## Read the markdown file
                    AI_NEWS_PATH = rf"./AINews/{frequency.lower()}_summary.md"
                    print(AI_NEWS_PATH)
                    with open(AI_NEWS_PATH, 'r',encoding='utf-8', errors='ignore') as file:
                        markdown_content = file.read()

                    st.markdown(markdown_content, unsafe_allow_html=False)
                except FileNotFoundError:
                    st.error("Error: Summary file not found. Please ensure the news fetching and summarization completed successfully.")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")







