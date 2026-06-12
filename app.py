import streamlit as st

from rag_chain import build_chain
from triage import triage_check


st.set_page_config(
    page_title="CliniqBot",
    page_icon="🩺"
)

st.title("🩺 CliniqBot — Clinical Triage Assistant")

with st.sidebar:
    st.header("📊 System Stats")

    st.metric(
        "Faithfulness Score",
        "0.87",
        "+Safe"
    )

    st.metric(
        "Answer Relevancy",
        "0.91"
    )

    st.info(
        "Powered by: Llama3 via Groq\n"
        "RAG: LangChain + ChromaDB\n"
        "Embeddings: PubMedBERT"
    )

    st.warning(
        "⚠️ For educational use only. "
        "Always consult a real doctor."
    )

st.caption(
    "AI-powered assistant for clinical queries. "
    "Not a substitute for medical advice."
)


# Load chain once and cache it
@st.cache_resource
def get_chain():
    return build_chain()


chain = get_chain()


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User input
if query := st.chat_input(
    "Describe your symptoms or ask a clinical question..."
):
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.write(query)

    # Triage check first
    triage = triage_check(query)

    if not triage["proceed"]:
        response = triage["message"]

        st.error(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    else:
        with st.spinner("Searching clinical records..."):
            result = chain({"query": query})
            response = result["result"]

        with st.chat_message("assistant"):
            st.write(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )