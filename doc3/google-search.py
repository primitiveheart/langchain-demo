import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType

os.environ["OPEN_API_KEY"] = "you are api key";
# https://serpapi.com/ 账号注册
os.environ["SERPAPI_API_KEY"] = "you are api key"

# 加载模型
llm = OpenAI(temperature=0, max_tokens=2048)
tools = load_tools(["serpapi"])
# 如果搜索完成想在计算一下可以这么写
# tools = load_tools(['serpapi', 'llm-math'])
# 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
# tools = load_tools(['serpapi', 'python_repl'])
# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("What's the date today? What great events have taken place today in history?")
