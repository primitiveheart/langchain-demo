from langchain.utilities import PythonREPL
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(model_name="gpt-3.5-turbo", max_tokens=2048, temperature=0.5)
math_chain = LLMChain(
    llm,
    prompt=PromptTemplate(template="请写一段Python代码，计算{question}?", input_variables=['question']),
    output_key="answer"
)
answer_code = math_chain.run({"question": "8452乘以18231"})
result = PythonREPL().run(answer_code) 
print(result)