import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamLitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit



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

    if user_message:
        try:
            ## configure the llms
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model= obj_llm_config.get_llm_model()

            if model is None:
                st.error("LLM model could not be initialized. Please check your configuration.")
                return
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("No use case selected. Please select a use case to proceed.")
                return
            st.success(f"LLM and Use Case '{usecase}',{model} configured successfully.")

            graph_builder = GraphBuilder(model=model)
            try:
                graph  = graph_builder.setup_graph(usecase=usecase)
                st.success("Graph Building Successfully.")
                DisplayResultStreamlit(usecase, graph , user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up graph for use case '{usecase}': {e}")
                return


        except Exception as e:
            st.error(f"An error occurred: {e}")
            return




    # Additional logic can be added here to utilize user_controls as needed