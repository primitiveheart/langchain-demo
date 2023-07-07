# Pinecone 是一个在线的向量数据库。所以，我可以第一步依旧是注册，然后拿到对应的 api key。https://app.pinecone.io/

from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

import pinecone

# 初始化 pinecone
pinecone.init(
  api_key="你的api key",
  environment="你的Environment"
)

loader = DirectoryLoader('/content/sample_data/data/', glob='**/*.txt')
# 将数据转成 document 对象，每个文件会作为一个 document
documents = loader.load()

# 初始化加载器
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
# 切割加载的 document
split_docs = text_splitter.split_documents(documents)

index_name="liaokong-test"

# 持久化数据
# docsearch = Pinecone.from_texts([t.page_content for t in split_docs], embeddings, index_name=index_name)

# 加载数据
docsearch = Pinecone.from_existing_index(index_name,embeddings)

query = "科大讯飞今年第一季度收入是多少？"
docs = docsearch.similarity_search(query, include_metadata=True)

llm = OpenAI(temperature=0)
chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
chain.run(input_documents=docs, question=query)