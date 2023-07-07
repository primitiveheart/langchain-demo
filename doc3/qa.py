import os 
from langchain.llms import OpenAI

os.environ["OPEN_API_KEY"] = "";

llm = OpenAI(model_name = "text_davinci-003", max_tokens=1024)
llm("怎么评价人工智能")

