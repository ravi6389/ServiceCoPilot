from langchain_openai import AzureOpenAIEmbeddings

from dotenv import load_dotenv

import os

load_dotenv()

# from config import (
#     AZURE_OPENAI_ENDPOINT,
#     AZURE_OPENAI_KEY,
#     AZURE_OPENAI_API_VERSION,
#     EMBEDDING_DEPLOYMENT
# )

# AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
# AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
# AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
# EMBEDDING_DEPLOYMENT = os.getenv("EMBEDDING_DEPLOYMENT")

# def get_embeddings():

#     embeddings = AzureOpenAIEmbeddings(

#         azure_endpoint=AZURE_OPENAI_ENDPOINT,

#         api_key=AZURE_OPENAI_KEY,

#         api_version=AZURE_OPENAI_API_VERSION,

#         azure_deployment=EMBEDDING_DEPLOYMENT

#     )

#     return embeddings

import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.embeddings import HuggingFaceEmbeddings

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

@st.cache_resource
def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name=MODEL_NAME,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )