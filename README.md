# End to End AgenticChatbot Project 🤖✨

A small Streamlit-based agentic chatbot workspace that demonstrates multiple use cases:
- Basic Chatbot
- Chatbot with Web / Tool integration
- AI News fetch & summarization

Quick links
- [app.py](app.py)
- [requirements.txt](requirements.txt)
- [`src.langgraphagenticai.main.load_langgraph_agenticai_app`](src/langgraphagenticai/main.py)
- [`src.langgraphagenticai.ui.streamlitui.display_result.DisplayResultStreamlit`](src/langgraphagenticai/ui/streamlitui/display_result.py)
- [`src.langgraphagenticai.graph.graph_builder.GraphBuilder`](src/langgraphagenticai/graph/graph_builder.py)
- [`src.langgraphagenticai.nodes.ai_news_node.AINewsNode`](src/langgraphagenticai/nodes/ai_news_node.py)
- [AINews/daily_summary.md](AINews/daily_summary.md)
- [.env](.env)
- [agenticaichat/LICENSE_PYTHON.txt](agenticaichat/LICENSE_PYTHON.txt)
- [src/__init__.py](src/__init__.py)

Overview 🧭
- The Streamlit UI loads user controls and then calls [`src.langgraphagenticai.main.load_langgraph_agenticai_app`](src/langgraphagenticai/main.py) to configure LLMs and graphs.
- Graphs are built with [`src.langgraphagenticai.graph.graph_builder.GraphBuilder`](src/langgraphagenticai/graph/graph_builder.py). Supported graphs:
  - Basic Chatbot
  - Chatbot with Tools
  - AI News pipeline (fetch -> summarize -> save)
- UI result rendering is handled by [`src.langgraphagenticai.ui.streamlitui.display_result.DisplayResultStreamlit`](src/langgraphagenticai/ui/streamlitui/display_result.py).
- The AI News logic is implemented in [`src.langgraphagenticai.nodes.ai_news_node.AINewsNode`](src/langgraphagenticai/nodes/ai_news_node.py). Summaries are written to the AINews folder (e.g., `./AINews/daily_summary.md`) by the node.

Prerequisites ✅
- Python 3.10+ recommended
- Create a virtual environment and install deps:
  ```sh
  python -m venv .venv
  source .venv/bin/activate   # or .venv\Scripts\activate on Windows
  pip install -r requirements.txt
  ```

Environment variables 🔐
- Populate a `.env` in the repo root (do not commit secrets!). The code references environment variables such as:
  - OPENAI_API_KEY
  - GROQ_API_KEY
  - TAVILY_API_KEY
  - LANGCHAIN_API_KEY / LANGSMITH_API_KEY
  - HUGGINGFACEHUB_API_TOKEN
  - PINECONE_API_KEY
  - and other third-party keys seen in the repo root `.env`
- Example (DO NOT paste real keys in commits):
  ```
  OPENAI_API_KEY="sk-..."
  GROQ_API_KEY="gsk-..."
  TAVILY_API_KEY="tvly-..."
  ```
- The AI News pipeline relies on the Tavily key and an LLM key to fetch and summarize news.

Running the app ▶️
- Run Streamlit (typical):
  ```sh
  streamlit run app.py
  ```
  If the project is structured to load Streamlit from `src`, adjust accordingly:
  ```sh
  streamlit run src/langgraphagenticai/main.py
  ```

AI News behavior 📰
- Use case "AI News" triggers the graph built by [`src.langgraphagenticai.graph.graph_builder.GraphBuilder.ai_news_builder_graph`](src/langgraphagenticai/graph/graph_builder.py).
- The news node [`src.langgraphagenticai.nodes.ai_news_node.AINewsNode`](src/langgraphagenticai/nodes/ai_news_node.py) fetches via Tavily, summarizes via the configured LLM, and writes a markdown file into `./AINews/{frequency}_summary.md` (e.g., `daily_summary.md`).
- Example saved summary: [AINews/daily_summary.md](AINews/daily_summary.md)

Troubleshooting & tips 🛠️
- If the LLM fails to initialize, check logs and verify environment variables for your LLM provider.
- If AI News summary file is missing, ensure Tavily fetch succeeded and the LLM returned a summary. Display logic lives in [`src.langgraphagenticai.ui.streamlitui.display_result.DisplayResultStreamlit`](src/langgraphagenticai/ui/streamlitui/display_result.py).
- To debug the graph creation or node behavior, inspect:
  - [`src.langgraphagenticai.graph.graph_builder.GraphBuilder`](src/langgraphagenticai/graph/graph_builder.py)
  - Node implementations in `src/langgraphagenticai/nodes/`

Development notes 🧩
- The project uses a simple StateGraph pattern (see `GraphBuilder`).
- Add or replace tool nodes under `src/langgraphagenticai/nodes/` and register them in `GraphBuilder.chatbot_with_tools_build_graph`.
- Avoid committing `.env` or any cleartext API keys.

Contributing 🤝
- Fork, implement small focused changes, open PRs with clear descriptions.
- Keep secrets out of commits.

License 📜
- See [agenticaichat/LICENSE_PYTHON.txt](agenticaichat/LICENSE_PYTHON.txt) for license details.

Contact / References 📎
- Open issues for bugs or feature requests.
- Refer to the code for entry points:
  - [`src.langgraphagenticai.main.load_langgraph_agenticai_app`](src/langgraphagenticai/main.py)
  - [`src.langgraphagenticai.ui.streamlitui.display_result.DisplayResultStreamlit`](src/langgraphagenticai/ui/streamlitui/display_result.py)
  - [`src.langgraphagenticai.graph.graph_builder.GraphBuilder`](src/langgraphagenticai/graph/graph_builder.py)
  - [`src.langgraphagenticai.nodes.ai_news_node.AINewsNode`](src/langgraphagenticai/nodes/ai_news_node.py)

Have fun building! 🚀