import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask Question About Your documents :")
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload Your PDF's here and click on Process" , accept_multiple_files=True)
        if st.button("Process"):
            

if __name__ == "__main__":
    main()