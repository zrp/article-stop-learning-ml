import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain.schema import HumanMessage, AIMessage
import time

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "knowledge_base" not in st.session_state:
        st.session_state.knowledge_base = None
    if "chain" not in st.session_state:
        st.session_state.chain = None

def process_pdf(pdf):
    """Process PDF and create knowledge base"""
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Create embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    
    return knowledge_base

def stream_response(response_text):
    """Stream the response text character by character"""
    message_placeholder = st.empty()
    full_response = ""
    
    for chunk in response_text.split():
        full_response += chunk + " "
        time.sleep(0.05)  # Small delay for streaming effect
        message_placeholder.markdown(full_response + "▌")
    
    message_placeholder.markdown(full_response)
    return full_response

def main():
    st.header("💬 Chat with your PDF")
    st.markdown("Upload a PDF and start a conversation with it!")

    # Initialize session state
    initialize_session_state()

    # Upload PDF
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf is not None:
        # Process PDF if not already done
        if st.session_state.knowledge_base is None:
            with st.spinner("Processing PDF..."):
                st.session_state.knowledge_base = process_pdf(pdf)
                st.session_state.chain = load_qa_chain(OpenAI(), chain_type="stuff")
            st.success("PDF processed successfully! You can now ask questions.")

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("Ask a question about your PDF:"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)

            # Get response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Get relevant documents
                    docs = st.session_state.knowledge_base.similarity_search(prompt)
                    
                    # Generate response
                    response = st.session_state.chain.run(input_documents=docs, question=prompt)
                    
                    # Stream the response
                    full_response = stream_response(response)
                    
                    # Add assistant message to chat history
                    st.session_state.messages.append({"role": "assistant", "content": full_response})

        # Sidebar with conversation controls
        with st.sidebar:
            st.header("Conversation Controls")
            
            if st.button("Clear Conversation"):
                st.session_state.messages = []
                st.rerun()
            
            st.markdown("---")
            st.markdown("**Conversation History:**")
            if st.session_state.messages:
                for i, msg in enumerate(st.session_state.messages):
                    role_icon = "👤" if msg["role"] == "user" else "🤖"
                    st.markdown(f"{role_icon} **{msg['role'].title()}:**")
                    st.markdown(f"_{msg['content'][:100]}{'...' if len(msg['content']) > 100 else ''}_")
                    if i < len(st.session_state.messages) - 1:
                        st.markdown("---")
            else:
                st.markdown("_No messages yet_")

if __name__ == '__main__':
    main()
