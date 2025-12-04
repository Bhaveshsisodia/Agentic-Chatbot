from langgraph.graph import StateGraph , START , END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chabot_node import BasicChabotNode
from src.langgraphagenticai.tools.search_tool import get_tools , create_tool_node
from langgraph.prebuilt import ToolNode, tools_condition
from src.langgraphagenticai.nodes.chatbot_with_Tool_node import ChatbotWithToolNode
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode

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

    def chatbot_with_tools_build_graph(self):

        """
        Builds a chatbot with tool integration using LangGraph.
        this methods creates a chatbot graph that inculudes both chatbot node and a tool node.
        it defines tools , initializes the nodes, and sets up the graph structure with appropriate edges.
        the chatbot node is configured to utilize the defined tools during its operation.
        """

        tools = get_tools()
        tool_node = create_tool_node(tools)

        obj_chatbot_with_node=ChatbotWithToolNode(self.llm,tools)

        chatbot_node = obj_chatbot_with_node.create_chatbot_node(tools)

        ## define the llmm


        ## define the chatbot node
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START , "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools" , "chatbot")
        self.graph_builder.add_edge("chatbot" , END)


    def ai_news_builder_graph(self):
        """Builds an AI News Explorer graph using LangGraph and then summarize it.
        This method sets up a graph that includes nodes for fetching and processing AI news based on user-defined time frames.
        It integrates a news fetching node and a chatbot node to provide an interactive experience for exploring AI news.
        """

        ai_news_node=AINewsNode(self.llm)
        ## added nodes
        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_results",ai_news_node.save_result)


        ## added edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge('fetch_news','summarize_news')
        self.graph_builder.add_edge('summarize_news','save_results')
        self.graph_builder.add_edge("save_results",END)
        print('AI News Graph Built Successfully')






    def setup_graph(self, usecase:str):
        """Sets up the graph based on the selected use case.
        Args:
            usecase (str): The use case selected by the user.
        Returns:
            StateGraph: The configured graph for the selected use case.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == 'Chatbot with Web':
            self.chatbot_with_tools_build_graph()

        if usecase == 'AI News':
            print("AI News Graph Building Started")
            self.ai_news_builder_graph()
            print("AI News Graph Building Completed")

        return self.graph_builder.compile()

