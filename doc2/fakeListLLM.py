import os 
from decouple import config
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.llms.fake import FakeListLLM

# 具体内容参考文档：https://testerhome.com/topics/36934

# os.environ["OPEN_API_KEY"] = config('OPENAI_API_KEY')

tools = load_tools(["python_repl"])
responses = [
    "Action: Python REPL \n Action Input: chatGpt原理",
    "Final Answer: mock答案"
]

llm = FakeListLLM(responses=responses)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("chatGpt原理2")