from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


VECTOR_DB = "vector_db"


def get_retriever():

    embedding = get_embeddings()

    db = Chroma(

        persist_directory=VECTOR_DB,

        embedding_function=embedding

    )

    return db.as_retriever(

        search_kwargs={

            "k": 3

        }

    )