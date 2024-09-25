from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.openai import OpenAI

# Define LLM
Settings.llm = OpenAI(temperature=0, model_name="gpt-4")

# Load documents
documents = SimpleDirectoryReader("backend/app/demo/docs").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Save index to disk
index.storage_context.persist(persist_dir="backend/app/demo/index")

# Query the index
query_engine = index.as_query_engine()
response = query_engine.query("What is the main topic of this document?")
print(response)
