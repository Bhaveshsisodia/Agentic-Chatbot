from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    A chatbot node that integrates tool functionalities.
    This class is designed to enhance chatbot capabilities by incorporating external tools for information retrieval and processing.
    """
    def __init__(self, model, tools):
        self.llm = model
        self.tools = tools

    def process(self, state:State) -> dict:
        """
        Process the user input and generate a response using the LLM model and integrated tools.
        Args:
            state (State): The current state containing user messages."""

        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.llm.invoke([{'role':'user', 'content': user_input}])

        tool_response = f"Tool Integration result for input: {user_input}"
        # Here you would implement the logic to utilize the tools along with the LLM
        # For simplicity, we will just return a placeholder response
        return {"messages": [llm_response, tool_response]}


    def create_chatbot_node(self, tools):
        """
        Creates and returns a chatbot node function that utilizes the provided tools."""

        llm_with_tools = self.llm.bind_tools(tools)
        def chatbot_node(state:State):

            """
            Chatbot Logic for processing the input state and returning a response."""
            return {"messages": [llm_with_tools.invoke(state['messages'])]}

        return chatbot_node


