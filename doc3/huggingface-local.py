# 将模型拉到本地使用的好处：
# 1.训练模型
# 2.可以使用本地的 GPU
# 3.有些模型无法在 HuggingFace 运行

from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM

model_id = 'google/flan-t5-large'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id, load_in_8bit=True)

pipe = pipeline(
    "text2text-generation",
    model=model, 
    tokenizer=tokenizer, 
    max_length=100
)

local_llm = HuggingFacePipeline(pipeline=pipe)
print(local_llm('What is the capital of France? '))


llm_chain = LLMChain(prompt=prompt,  llm=local_llm)
question = "What is the capital of England?"
print(llm_chain.run(question))