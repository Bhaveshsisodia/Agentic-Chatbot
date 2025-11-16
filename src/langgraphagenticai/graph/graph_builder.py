from langgraph.graph import StateGraph , START , END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chabot_node import BasicChabotNode

class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """Builds a basic chatbot using LangGraph.
        This mehtods initializes a chatbot node using the `BasicChatbotNode` class and integrates it into the graph.
        The chatbot node is set as both the entry and exit point of the graph.

        """

        self.basic_chatbot_node = BasicChabotNode(self.llm)
        ## node addition
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)

        ## edge addition
        self.graph_builder.add_edge(START , "chatbot")
        self.graph_builder.add_edge("chatbot" , END)


    def setup_graph(self, usecase:str):
        """Sets up the graph based on the selected use case.
        Args:
            usecase (str): The use case selected by the user.
        Returns:
            StateGraph: The configured graph for the selected use case.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            
        return self.graph_builder.compile()

