# 使用 Langchian 提供的 HumanInputLLM，访问维基百科查询
from langchain.llms.human import HumanInputLLM
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from wikipedia import set_lang

tools = load_tools(["wikipedia"])
# 这里必须要设置为中文 url 前缀，不然访问不了
set_lang('zh')

llm = HumanInputLLM(prompt_func=lambda prompt: print(f"\n===PROMPT====\n{prompt}\n=====END OF PROMPT======"))
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("喜羊羊")