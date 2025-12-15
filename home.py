import streamlit as st
import backend as rag


st.title("Recommendation System with RAG Pipeline")
st.subheader("MLH Global Hack Week AI/ML 2025")
st.divider()

#Create a sidebar
#Upload in here the context that goes into MongoDB (Knowledgebase)
with st.sidebar:
    st.header("Upload your Context")
    user_text=st.text_area("Enter text to add to the knowledge base", height=150)

    if st.button("Upload to MongoDB"):
        if user_text:
            with st.spinner("Uploading to MongoDB..."):
                rag.ingest_text(user_text)
                st.success("Text uploaded successfully!")
        else:
            st.error("Please enter text before uploading.")