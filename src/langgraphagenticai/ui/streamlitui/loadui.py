import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamLitUI:
    def __init__(self):

        
        self.config = Config()
        self.page_title = self.config.get_page_title()
        self.llm_options = self.config.get_llm_options()
        self.usecase_options = self.config.get_usecase_options()
        self.groq_model_options = self.config.get_groq_model_options()
        self.user_controls = {}



    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖" +self.page_title , layout="wide" )
        st.header("🤖 " + self.page_title)

        with st.sidebar:
            st.header("Configuration Options")
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", self.llm_options)

            if self.user_controls['selected_llm'] == "Groq":

                self.user_controls['selected_groq_model'] = st.selectbox("Select GROQ Model", self.groq_model_options)
                self.user_controls['GROQ_API_KEY']=st.session_state['GROQ_API_KEY']=st.text_input("Enter your Groq API Key", type="password")

                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("⚠️ Please enter your Groq API Key to proceed.‼️")


            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", self.usecase_options)

        return self.user_controls



