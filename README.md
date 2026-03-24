# Hugging Face Inference API for Embeddings
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Inference%20API-orange)](https://huggingface.co/docs/api-inference/index)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Serverless](https://img.shields.io/badge/Cloud-Serverless-red)](https://en.wikipedia.org/wiki/Serverless_computing)

## 🚀 Project Overview
This repository demonstrates how to utilize the **Hugging Face Inference API** to generate high-quality text embeddings without the need for local GPU hardware. By interfacing with the Hugging Face Hub, this project enables the use of thousands of specialized embedding models (such as BGE, GTE, and Sentence-Transformers) through a simple, scalable REST API.

---

## 🛠️ Key Technical Implementations

### 1. Hosted Inference Pipeline
* **Model Orchestration:** Accessing state-of-the-art open-source embedding models via the `InferenceClient`.
* **Zero-Infrastructure Vectors:** Generating embeddings in the cloud, significantly reducing local computational overhead.

### 2. Multi-Model Benchmarking
* **Model Versatility:** Easily switching between small, fast models (e.g., `all-MiniLM-L6-v2`) and high-accuracy models (e.g., `BAAI/bge-large-en-v1.5`).
* **Feature Comparison:** Analyzing how different model architectures represent the same text in vector space.

### 3. Semantic Search Logic
* **Query-to-Vector Transformation:** Converting natural language into 384, 768, or 1024-dimensional vectors.
* **Similarity Scoring:** Implementing Cosine Similarity to rank document relevancy based on API-generated vectors.

### 4. Production Best Practices
* **Secure Authentication:** Using `HF_TOKEN` and `.env` files to protect API credentials.
* **Wait-for-Model Logic:** Implementing retry mechanisms to handle model "cold starts" on the Inference API.

---

## 💻 Tech Stack
* **Language:** Python
* **SDK:** `huggingface_hub`
* **Mathematics:** NumPy, SciPy
* **Environment:** `python-dotenv`
* **Platform:** Jupyter Notebook / Google Colab
