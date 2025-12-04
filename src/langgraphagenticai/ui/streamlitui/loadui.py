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

        st.session_state.timeframe = ""
        st.session_state["IsFetchButtonClicked"] = False
        with st.sidebar:
            st.header("Configuration Options")
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", self.llm_options)

            if self.user_controls['selected_llm'] == "Groq":

                self.user_controls['selected_groq_model'] = st.selectbox("Select GROQ Model", self.groq_model_options)
                self.user_controls['GROQ_API_KEY']=st.session_state['GROQ_API_KEY']=st.text_input("Enter your Groq API Key", type="password")

                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("⚠️ Please enter your Groq API Key to proceed.‼️")


            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", self.usecase_options)

            if self.user_controls['selected_usecase'] == "Chatbot with Web" or self.user_controls['selected_usecase'] == "AI News":
                os.environ['TAVILY_API_KEY']=self.user_controls['TAVILY_API_KEY'] = st.session_state['TAVILY_API_KEY'] = st.text_input("Enter your Tavily API Key", type="password") #st.text_input("Enter your Tavily API Key", type="password")

                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning("⚠️ Please enter your Tavily API Key to proceed.‼️ refer https://www.tavily.com/ to get your API Key.")

            if self.user_controls['selected_usecase'] == "AI News":
                st.subheader("AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "Select Time Frame",
                        ["Daily", "Weekly", "Monthly"], index=0)

                if st.button("Fetch Latest AI News",use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True

                    st.session_state.timeframe = time_frame

            print(self.user_controls)






        return self.user_controls



