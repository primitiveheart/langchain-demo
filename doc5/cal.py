from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

a, b = 8452, 18231
math_chain = LLMChain(
    llm=OpenAI(model_name="gpt-3.5-turbo", max_tokens=2048, temperature=0.5),
    prompt=PromptTemplate(template="请计算一下{question}是多少?", input_variables=["question"]),
    output_key="answer"
)
chatgpt_answer = math_chain.run({"question": f"{a}乘以{b}，只回答结果"})
print("ChatGPT 说答案是:", chatgpt_answer)

# python_answer = a * b
# print("Python 说答案是:", python_answer)