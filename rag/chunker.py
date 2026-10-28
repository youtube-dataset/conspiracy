import json

from langchain_text_splitters import RecursiveCharacterTextSplitter

def return_conspiracy_theories_titles():
    data_path = "./data/conspiracy_theories_data.json"

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [d["title"] for d in data]


def chunk_titles(titles=None):
    titles = return_conspiracy_theories_titles()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=0
    )

    # create_documents splits the list of title strings into LangChain Document chunks
    chunks = text_splitter.create_documents(titles)
    return chunks


if __name__ == "__main__":
    chunks = chunk_titles()
    print(f"Total chunks created: {len(chunks)}")
    for i, chunk in enumerate(chunks[:5]):
        print(f"Chunk {i+1}: {chunk.page_content}")
