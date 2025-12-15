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

st.header("Ask Chat anything from our Knowledge Base")

#Intialize the whole message history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Handle user input
prompt = st.chat_input("Ask any question to the chat")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate rag response in here
    with st.chat_message("ROBOT"):
        with st.spinner("THINKINGSS"):
            response_data = rag.get_rag_response(prompt)
            answer = response_data["answer"]
            sources = response_data["sources"]

            st.markdown(answer)

            # show sources in a expander
            with st.expander("Sources"):
                for i, source in enumerate(sources):
                    st.markdown(f"**Source {i+1}:** {source.page_content}")
            # Append the response to the message history
            st.session_state.messages.append({"role": "ROBOT", "content": answer})