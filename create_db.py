#load pdf
#split intochunk
#create the embedding
#store into chroma
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

data= PyPDFLoader("Document Loaders/RAG_AI_Document.pdf")
docs = data.load()



splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 5
)
chunks = splitter.split_documents(docs)
print("Chunks created:", len(chunks))
embedding_model = MistralAIEmbeddings()

vectorstore = Chroma.from_documents(
     documents=chunks,
     embedding=embedding_model,
     persist_directory="chroma-db"
)
