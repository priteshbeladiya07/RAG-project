from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
url = "https://www.samsung.com/in/smartphones/galaxy-s25/?srsltid=AfmBOorPQxeFCy8MjQzvkkMIcNyZjyuu5W-_PmyTVAiOhFb1FIQNtb43"
data = WebBaseLoader(url)
docs = data.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap =1
)
chunks =splitter.split_documents(docs)
print(chunks[0].page_content)