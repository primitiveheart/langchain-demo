# 主要是结合使用 zapier 来实现将万种工具连接起来。
# 申请账号和他的自然语言 api key。https://zapier.com/l/natural-language-actions 
# 右键里面的连接打开我们的api 配置页面。我们点击右侧的 Manage Actions 来配置我们要使用哪些应用。
import os
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper

os.environ["ZAPIER_NLA_API_KEY"] = ''

llm = OpenAI(temperature=.3)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)

# 我们可以通过打印的方式看到我们都在 Zapier 里面配置了哪些可以用的工具
for tool in toolkit.get_tools():
  print (tool.name)
  print (tool.description)
  print ("\n\n")

agent.run('请用中文总结最后一封"******@qq.com"发给我的邮件。并将总结发送给"******@qq.com"')