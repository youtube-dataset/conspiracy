import os
from dotenv import load_dotenv
from pinecone import Pinecone
from chunker import chunk_titles

# Load environment variables from the .env file
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

def pinecone_index():
    index_name = "conspiracy-theories-vector-index"
    
    existing_indexes = [idx.name for idx in pc.list_indexes()]
    if index_name not in existing_indexes:
        pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model": "llama-text-embed-v2",
                "field_map": {"text": "chunked_titles"}                  
            }
        )

    index = pc.index(index_name)
    chunks = chunk_titles()

    # Extract text.page_content and use a clean ID format without spaces
    records = [
        {"_id": f"chunk-{i}", "chunked_titles": doc.page_content}
        for i, doc in enumerate(chunks)
    ]

    index.upsert_records(namespace="conspiracy_theories_namespace", records=records)
    print(f"Successfully upserted {len(records)} records to Pinecone!")

if __name__ == "__main__":
    pinecone_index()