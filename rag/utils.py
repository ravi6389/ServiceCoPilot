from langchain_core.documents import Document

import pandas as pd


def load_ticket_documents(csv_path):

    df = pd.read_csv(csv_path)

    documents = []

    for _, row in df.iterrows():

        text = f"""

Ticket ID : {row['TicketID']}

Machine : {row['Machine']}

Error Code : {row['ErrorCode']}

Problem :

{row['Problem']}

Root Cause :

{row['RootCause']}

Resolution :

{row['Resolution']}

Parts :

{row['Parts']}

Engineer Notes :

{row['EngineerNotes']}

"""

        doc = Document(

            page_content=text,

            metadata={

                "ticket_id": row["TicketID"],

                "machine": row["Machine"],

                "error": row["ErrorCode"]

            }

        )

        documents.append(doc)

    return documents