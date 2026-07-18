from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter
data = PyPDFLoader("Document Loaders/RAG_AI_Document.pdf")
docs = data.load()
splitter = TokenTextSplitter(
    chunk_size = 10,
    chunk_overlap=1
)
chunks = splitter.split_documents(docs)
print(chunks[0].page_content)