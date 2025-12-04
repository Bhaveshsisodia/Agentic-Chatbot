from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime

class AINewsNode:

    def __init__(self, llm):
        """Initializes the AI News Node with a language model and Tavily client."""

        self.tavily = TavilyClient()
        self.llm = llm

        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """Fetches AI news based on the specified time frame and updates the state.

        Args:
            state (dict): The current state containing user inputs.
        Returns:
            dict: The updated state with fetched news articles."""

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map ={'daily':'d','weekly':'w','monthly':'m','yearly': 'y'}
        days_map ={'daily':1,'weekly':7,'monthly':30,'yearly':366}

        response = self.tavily.search(
            query = "Top Artificial Intelligence News in India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=20,
            days = days_map[frequency],
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        # print(self.state['news_data'])
        return state

    def summarize_news(self, state: dict) -> dict:
        """Summarizes the fetched news articles and updates the state.

        Args:
            state (dict): The current state containing fetched news articles.
        Returns:
            dict: The updated state with the summary of news articles."""

        news_items = self.state['news_data']

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """summarize the following AI news articles into markdown format. for each item include:
             - Date in **YYYY-MM-DD** format in IST timezone
             - concise sentences summary from latest news
             - sort news by date wise (latest first)
             - source link for each news item
             use format:
             ### [Date]
             -[Summary](URL)"""),
             ("user","Articles:\n{articles}")

        ])

        articles_str = "\n".join(
            [f"Content: {item.get('content','')}\nURL: {item.get('url','')}\nDate: {item.get('published_date',"")}" for item in news_items])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))

        state['summary']= response.content
        self.state['summary'] = state['summary']
        print(self.state['summary'])
        return self.state

    def save_result(self,state):
        import re

        frequency = re.sub(r'[^\w\-]', '_', self.state['frequency'])

        summary = self.state['summary']
        filename = fr"./AINews/{frequency}_summary.md"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"#{frequency.capitalize()} AI News Summary\n\n")
            file.write(summary)

        self.state['filename'] = filename
        return self.state
