from langchain_chroma import Chroma

from rag.embeddings import get_embeddings

from rag.utils import load_ticket_documents


CSV_PATH = "data/historical_tickets.csv"

VECTOR_DB = "vector_db"


def create_vector_db():

    print("Loading historical tickets...")

    docs = load_ticket_documents(CSV_PATH)

    print(f"Loaded {len(docs)} tickets")

    embedding = get_embeddings()

    print("Creating ChromaDB...")

    Chroma.from_documents(

        documents=docs,

        embedding=embedding,

        persist_directory=VECTOR_DB

    )

    print("Done.")


if __name__ == "__main__":

    create_db()
