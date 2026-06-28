# import streamlit as st

# from rag.chatbot import ask_service_engineer

# st.set_page_config(
#     page_title="Service Engineer Copilot",
#     page_icon="🛠️",
#     layout="wide"
# )

# st.title("🛠️ Service Engineer Copilot")

# st.markdown(
# """
# AI-powered assistant that helps Service Engineers solve customer issues
# using historical service tickets.
# """
# )

# st.divider()

# # -------------------------------
# # Input Section
# # -------------------------------

# left, right = st.columns([2, 1])

# with left:

#     machine = st.text_input(
#         "Machine Model",
#         placeholder="Compressor A"
#     )

#     error = st.text_input(
#         "Error Code",
#         placeholder="E101"
#     )

#     problem = st.text_area(
#         "Describe Customer Issue",
#         height=220,
#         placeholder="""
# Example

# Machine becomes hot after 20 minutes.

# Cooling fan running slowly.

# Customer reports burning smell.
# """
#     )

#     analyse = st.button(
#         "Analyze Problem",
#         use_container_width=True,
#         type="primary"
#     )

# with right:

#     st.info(
# """
# ### Example

# **Machine**

# Compressor A

# **Error**

# E101

# **Problem**

# Machine overheats after 20 minutes.

# Cooling fan RPM is low.
# """
#     )

# # -------------------------------------
# # AI
# # -------------------------------------

# if analyse:

#     if problem.strip() == "":

#         st.warning("Please describe the customer issue.")

#         st.stop()

#     query = f"""

# Machine : {machine}

# Error Code : {error}

# Problem :

# {problem}

# """

#     with st.spinner("Searching historical service tickets..."):

#         answer, docs = ask_service_engineer(query)

#     st.divider()

#     st.subheader("🛠 AI Recommendation")

#     st.success(answer)

#     st.divider()

#     st.subheader("📚 Historical Tickets Used")

#     for i, doc in enumerate(docs, start=1):

#         with st.expander(f"Historical Ticket {i}"):

#             st.write(doc.page_content)

#             st.markdown("### Metadata")

#             st.json(doc.metadata)


import streamlit as st

from rag.chatbot import ask_service_engineer
import os

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.write("Current working directory:", os.getcwd())

st.write("vector_db exists:", os.path.exists("vector_db"))

st.write(
    "chroma.sqlite3 exists:",
    os.path.exists("vector_db/chroma.sqlite3")
)

if os.path.exists("vector_db"):
    st.write("Files inside vector_db:")
    st.write(os.listdir("vector_db"))
if not os.path.exists("vector_db/chroma.sqlite3"):
    st.write('vector_db doesnt exist')
    from rag.create_vector_db import create_vector_db
    create_vector_db()
    
st.set_page_config(
    page_title="Service Engineer Copilot",
    page_icon="🛠",
    layout="wide"
)

# ---------------------------------------------------

if "answer" not in st.session_state:
    st.session_state.answer = None

if "docs" not in st.session_state:
    st.session_state.docs = []

# ---------------------------------------------------

st.title("🛠 Service Engineer Copilot")

st.caption(
    "AI powered troubleshooting assistant using Retrieval Augmented Generation (RAG)"
)

st.divider()

# ---------------------------------------------------

left, right = st.columns([2,1])

# ===================================================
# LEFT PANEL
# ===================================================

with left:

    st.subheader("Customer Issue")

    machine = st.text_input(
        "Machine Model",
        placeholder="Compressor A"
    )

    error = st.text_input(
        "Error Code",
        placeholder="E101"
    )

    problem = st.text_area(
        "Problem Description",
        height=220,
        placeholder="""
Machine overheats after 20 minutes.

Cooling fan RPM is low.

Burning smell observed.
"""
    )

    if st.button(
        "🔍 Analyze Problem",
        type="primary",
        use_container_width=True
    ):

        query = f"""
Machine : {machine}

Error Code : {error}

Problem :

{problem}
"""

        with st.spinner("Searching historical tickets..."):

            answer, docs = ask_service_engineer(query)

        st.session_state.answer = answer
        st.session_state.docs = docs

# ===================================================
# RIGHT PANEL
# ===================================================

with right:

    st.subheader("Retrieved Tickets")

    if len(st.session_state.docs)==0:

        st.info(
            "Historical tickets will appear here after analysis."
        )

    else:

        for doc in st.session_state.docs:

            ticket = doc.metadata["ticket_id"]

            machine = doc.metadata["machine"]

            error = doc.metadata["error"]

            with st.expander(
                f"🎫 {ticket}"
            ):

                st.write(f"**Machine** : {machine}")

                st.write(f"**Error Code** : {error}")

                st.markdown("---")

                st.write(doc.page_content)

# ===================================================
# AI REPORT
# ===================================================

if st.session_state.answer:

    st.divider()

    st.subheader("🛠 AI Service Engineer Report")

    st.markdown(st.session_state.answer)
