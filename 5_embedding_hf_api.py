import os
import sys

# 1. THE PERMANENT DLL FIX
# We must block 'torch' before importing any LangChain HuggingFace tools
# to prevent the WinError 1114 (c10.dll) crash.
os.environ["USE_TORCH"] = "FALSE"
sys.modules["torch"] = None 

from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

# 2. LOAD ENVIRONMENT VARIABLES
load_dotenv()

# 3. INITIALIZE THE EMBEDDING MODEL
# This uses the Hugging Face API (Serverless), avoiding local hardware issues.
embeddings_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# 4. DEFINE YOUR DOCUMENTS
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

try:
    print("--- Connecting to Hugging Face API ---")
    
    # 5. GENERATE THE RAW VECTORS (The model defaults to 384 dimensions)
    raw_vectors = embeddings_model.embed_documents(documents)
    
    # 6. SLICE TO 32 DIMENSIONS
    # Since you specifically need 32 values per vector for your project:
    final_vectors = [vec[:32] for vec in raw_vectors]
    
    # 7. DISPLAY THE RESULTS
    print(f"✅ Success! Generated {len(final_vectors)} vectors.")
    
    for i, vector in enumerate(final_vectors):
        print(f"\nVector {i+1} (32 Dimensions):")
        print(vector)
        print(f"Count: {len(vector)}")

except Exception as e:
    print(f"❌ Error occurred: {e}")