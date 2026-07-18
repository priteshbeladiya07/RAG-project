from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

data = PyPDFLoader("Document Loaders/RAG_AI_Document.pdf")

model = ChatMistralAI(model = "mistral-small-2506")

docs = data.load()
template = ChatPromptTemplate.from_messages(
    [
        ("system","you are a AI that summarizes the text"),
        ("human","{data}")
    ]
)

prompt = template.format_messages(data = docs)
result = model.invoke(prompt)
print(result.content)



