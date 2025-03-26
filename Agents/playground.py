from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import phi.api
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv


import os
import phi
from phi.playground import Playground, serve_playground_app
load_dotenv()

phi.api = os.getenv('PHI_API_KEY')

# Web Search Agent

websearch_agent = Agent(
    name='web search agent',
    role='Search the web for information',
    model=Groq(id='llama-3.3-70b-specdec'),
    tools=[DuckDuckGo()],
    instructions=['Always include sources in your search results'],
    show_tool_calls=True,
    markdown=True,
)

## Financial Agent

distance_agent = Agent(
    name = 'Financial Agent',
    model = Groq(id='llama-3.3-70b-specdec'),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)
    ],
    instructions=['use tables to display data'],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[distance_agent, websearch_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app('playground:app', reload=True)