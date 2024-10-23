from .tools import *
import yaml
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor

def gpt_agent(instructions, url, openai_api_key):
    with open("RuFus/prompts.yaml", 'r') as file:
            sys_pmt = yaml.safe_load(file)

    tools = [get_sitemap]
    prompt = ChatPromptTemplate.from_messages([
            ("system",sys_pmt["sys_prompt"] ),
            ("user", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key = openai_api_key)

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    rel_links = eval(agent_executor.invoke({"input": f"query: {instructions}, url:{url}"}).get('output'))
    return rel_links
