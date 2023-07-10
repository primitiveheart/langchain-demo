# langchain-demo
langchain 示例


# 第一部分 学习文档
学习参考文档：
文档一：官方文档，https://python.langchain.com/docs/get_started/introduction.html
文档二：https://www.cnblogs.com/leeronggui/p/5380050.html
文档三：https://www.langchain.cn/t/topic/35 & https://liaokong.gitbook.io/llm-kai-fa-jiao-cheng/
文档四：LangChain+LLM 被低估的few-shot魔法 https://www.langchain.cn/t/topic/18

# 第二部 名词解释
名词解释
参数一：关于agent type 几个选项的含义（理解不了也不会影响下面的学习，用多了自然理解了）：
zero-shot-react-description: 根据工具的描述和请求内容的来决定使用哪个工具（最常用）
react-docstore: 使用 ReAct 框架和 docstore 交互, 使用Search 和Lookup 工具, 前者用来搜, 后者寻找term, 举例: Wipipedia 工具
self-ask-with-search 此代理只使用一个工具: Intermediate Answer, 它会为问题寻找事实答案(指的非 gpt 生成的答案, 而是在网络中,文本中已存在的), 如 Google search API 工具
conversational-react-description: 为会话设置而设计的代理, 它的prompt会被设计的具有会话性, 且还是会使用 ReAct 框架来决定使用来个工具, 并且将过往的会话交互存入内存

参数二：chain 的 chain_type 参数
这个参数主要控制了将 document 传递给 llm 模型的方式，一共有 4 种方式：
stuff : 这种最简单粗暴，会把所有的 document 一次全部传给 llm 模型进行总结。如果document很多的话，势必会报超出最大 token 限制的错，所以总结文本的时候一般不会选中这个。

map_reduce : 这个方式会先将每个 document 进行总结，最后将所有 document 总结出的结果再进行一次总结。

refine : 这种方式会先总结第一个 document，然后在将第一个 document 总结出的内容和第二个 document 一起发给 llm 模型在进行总结，以此类推。这种方式的好处就是在总结后一个 document 的时候，会带着前一个的 document 进行总结，给需要总结的 document 添加了上下文，增加了总结内容的连贯性。

map_rerank : 这种一般不会用在总结的 chain 上，而是会用在问答的 chain 上，他其实是一种搜索答案的匹配方式。首先你要给出一个问题，他会根据问题给每个 document 计算一个这个 document 能回答这个问题的概率分数，然后找到分数最高的那个 document ，在通过把这个 document 转化为问题的 prompt 的一部分（问题+document）发送给 llm 模型，最后 llm 模型返回具体答案。


名称	描述
Apify	一个网络爬虫和自动化工具的平台
Arxiv API	arXiv预印本数据库的API
Bash	一种Linux和Unix操作系统的命令行语言
Bing Search	微软的搜索引擎
ChatGPT Plugins	ChatGPT模型的插件，提供额外的功能和定制化选项
DuckDuckGo Search	一个隐私保护的搜索引擎
Google Places	Google提供的本地商家信息的服务
Google Search	Google的搜索引擎
Google Serper API	Google搜索结果的API
Gradio Tools	一个用于构建和部署自定义机器学习应用程序的开源工具
Human as a tool	将人的智力作为工具来解决问题
IFTTT WebHooks	一个可以将应用程序和设备连接起来的自动化服务
OpenWeatherMap API	提供全球天气预报和历史数据的API
Python REPL	Python的交互式解释器
Requests	一个Python库，用于向Web服务器发出HTTP请求并获取响应
Search Tools	用于在互联网上搜索信息的工具
SearxNG Search API	一个元搜索引擎的API，可以从多个搜索引擎收集结果
SerpAPI	提供各种搜索引擎的搜索结果的API
Wikipedia API	提供维基百科内容的API
Wolfram Alpha	一个基于自然语言理解的计算知识引擎，可回答各种问题和计算结果
Zapier Natural Language Actixin	可以访问Zapier平台上的5,000多个应用程序和20,000多个操作


# 第三部分：python 依赖

python 依赖的包
安装依赖：pip install python-decouple
导入方式：from decouple import config
用途：将设置从代码中分离开，decouple将帮助你解析你的程序配置文件，达到更改你的设置而不用重新部署程序的效果
参考文档：https://www.cnblogs.com/leeronggui/p/5380050.html


pip install wikipedia