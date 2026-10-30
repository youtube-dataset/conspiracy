import os,time

from dotenv import load_dotenv
from pinecone import Pinecone, SchemaBuilder
from chunker import chunk_titles

pc = Pinecone(api_key=os.environ.get["PINECONE_API_KEY"])

