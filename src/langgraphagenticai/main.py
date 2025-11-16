import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamLitUI


def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI Streamlit application.
    Returns:
        dict: A dictionary containing user-selected controls from the UI.
    """


    ## load ui

    ui = LoadStreamLitUI()
    user_input = ui.load_streamlit_ui()
    if not user_input:
        st.error("Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message here:")
    



    # Additional logic can be added here to utilize user_controls as needed