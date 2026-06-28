# from langchain_openai import AzureChatOpenAI

# from langchain.prompts import ChatPromptTemplate

# from rag.prompt import SYSTEM_PROMPT

# from rag.retriever import get_retriever

# from config import (
#     AZURE_OPENAI_ENDPOINT,
#     AZURE_OPENAI_KEY,
#     AZURE_OPENAI_API_VERSION,
#     CHAT_DEPLOYMENT
# )

# llm = AzureChatOpenAI(

#     azure_endpoint=AZURE_OPENAI_ENDPOINT,

#     api_key=AZURE_OPENAI_KEY,

#     api_version=AZURE_OPENAI_API_VERSION,

#     azure_deployment=CHAT_DEPLOYMENT,

#     temperature=0

# )

# retriever = get_retriever()

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", SYSTEM_PROMPT),
#         ("human", "{question}\n\nContext:\n{context}")
#     ]
# )


# def ask_service_engineer(question):

#     docs = retriever.invoke(question)

#     context = "\n\n".join(
#         doc.page_content for doc in docs
#     )

#     chain = prompt | llm

#     answer = chain.invoke(
#         {
#             "question": question,
#             "context": context
#         }
#     )

#     return answer.content, docs
from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from rag.prompt import SYSTEM_PROMPT

from rag.llm import llm

from rag.retriever import get_retriever


retriever = get_retriever()


def ask_service_engineer(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    messages = [

        SystemMessage(
            content=SYSTEM_PROMPT
        ),

        HumanMessage(
            content=f"""

Customer Question

{question}


Historical Tickets

{context}

"""
        )
    ]

    response = llm.invoke(messages)

    return response.content, docs