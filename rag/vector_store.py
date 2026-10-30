import os
from dotenv import load_dotenv
from pinecone import Pinecone
from chunker import chunk_titles
# Load environment variables from the .env file
load_dotenv()

# Initialize Pinecone using proper method/lookup syntax
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

def pinecone_index():
    pc.create_index_for_model(
        name="conspiracy_theories_vector_index",
        cloud="aws",
        region="us-east-1",
        embed= {
            "model": "llama-text-embed-v2",
            "field_map": {"text": chunk_titles}  # map your chunk text field                    
        }
    )