from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
url = "https://www.samsung.com/in/smartphones/galaxy-s25/?srsltid=AfmBOorPQxeFCy8MjQzvkkMIcNyZjyuu5W-_PmyTVAiOhFb1FIQNtb43"
data = WebBaseLoader(url)

model = ChatMistralAI(model = "mistral-small-2506")

docs = data.load()
template = ChatPromptTemplate.from_messages(
    [
        ("system","you are a AI that summarizes the text"),
        ("human","{data}")
    ]
)

prompt = template.format_messages(data = docs[0].page_content)
result = model.invoke(prompt)
print(result.content)



