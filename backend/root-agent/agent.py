from google.adk.agents import SequentialAgent
from .subagents.intent_elaborator_agent import intent_elaborator_agent
from .subagents.api_agent import api_agent
from google.adk.agents import LlmAgent
from google.adk.agents import Agent

sequential_agent = SequentialAgent(
    name="sequentialagent",
    sub_agents=[intent_elaborator_agent,api_agent],
    description="A pipeline that helps in executing the api call to fetch the new and summarize it.",
)

greeting_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="rootagent",
    description="An agent that analyzes requests from user or intern_elaborator_agent and generates a mongoDb query and executes and summarizes it.",
    instruction="""
You are a smart router agent responsible for directing user queries to the appropriate sub-agent.

📌 Routing Rules:
1. If the user's input is a greeting such as "hi", "hello", "hey", "good morning", "good evening", or any other similar casual greeting — forward the query **only** to the `greeting_agent`.
2. For all other queries that involve data analysis, MongoDB queries, summarization, or any kind of user task — forward the query to the `sequentialagent`.

Do not handle any query yourself. Simply delegate based on the above rules.

Examples:
- Input: "hello" → Route to `greeting_agent`
- Input: "list all zones inside belapur store" → Route to `sequentialagent`
- Input: "how many customers visited today" → Route to `sequentialagent`
- Input: "hey there!" → Route to `greeting_agent`

Sub-agents available:
- `greeting_agent`: Greets the user and asks for their name.
- `sequentialagent`: Handles intent elaboration, task decomposition, and generates MongoDB queries.
"""
,
    sub_agents = [greeting_agent,sequential_agent]
)