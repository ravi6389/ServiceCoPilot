from langchain_openai import AzureChatOpenAI

from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_CHAT_DEPLOYMENT
)

llm = AzureChatOpenAI(

    azure_endpoint=AZURE_OPENAI_ENDPOINT,

    api_key=AZURE_OPENAI_KEY,

    api_version=AZURE_OPENAI_API_VERSION,

    azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,

    temperature=0

)