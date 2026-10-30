import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

def return_conspiracy_theories_titles():
    data_path = "./data/conspiracy_theories_data.json"

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [d["title"] for d in data]

def chunk_titles(chunk_size: int = 100, chunk_overlap: int = 20):
    titles = return_conspiracy_theories_titles()
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.create_documents(titles)

print(chunk_titles())