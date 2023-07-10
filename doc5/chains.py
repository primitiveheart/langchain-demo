from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

llm = OpenAI(model_name="gpt-3.5-turbo", max_tokens=2048, temperature=0.5)

chinese_qa_chain = SimpleSequentialChain(chains=[
    LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["chinese_question"],
            template="请把下面这句话翻译成英文： \n\n {chinese_question}?"),
        output_key="english_question"
    ),
    LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["english_question"],
            template="{english_question}"),
        output_key="english_answer"
    ),
    LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["english_answer"],
            template="请把下面这一段翻译成中文： \n\n{english_answer}?"),
        output_key="chinese_answer"
    )
], input_key="chinese_question", verbose=True)

chinese_question = input()
chinese_answer = chinese_qa_chain.run(chinese_question=chinese_question)
print(chinese_answer)