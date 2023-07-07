from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import HuggingFaceHub
import os
from decouple import config

from langchain.agents import load_tools


os.environ["HUGGINGFACEHUB_API_TOKEN"] = config('HUGGINGFACEHUB_API_TOKEN')

# 导入文本
loader = UnstructuredFileLoader("docment_store\helloLangChain.txt")
# 将文本转成 Document 对象
document = loader.load()
print(f'documents:{len(document)}')
# 初始化文本分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 0
)
# 切分文本
split_documents = text_splitter.split_documents(document)
print(f'documents:{len(split_documents)}')
# 加载 LLM 模型
overal_temperature = 0.1
flan_t5xxl = HuggingFaceHub(repo_id="google/flan-t5-xxl", 
                         model_kwargs={"temperature":overal_temperature, 
                                       "max_new_tokens":200}
                         ) 

llm = flan_t5xxl
tools = load_tools(["llm-math"], llm=llm)
# 创建总结链
chain = load_summarize_chain(llm, chain_type="refine", verbose=True)
# 执行总结链
chain.run(split_documents)




