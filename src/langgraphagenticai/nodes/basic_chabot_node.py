from src.langgraphagenticai.state.state import State



class BasicChabotNode:
    """
    A basic chatbot node for handling user interactions.
    This class serves as a foundational component for building chatbot functionalities within the LangGraph framework.
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state:State)-> dict:
        """
        Process the user input and generate a response using the LLM model.
        Args:
            state (State): The current state containing user messages."""
        return {"messages":self.llm.invoke(state['messages'])}
