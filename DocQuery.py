#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import streamlit as st
from docquery import pipeline

# Load the Document Question Answering pipeline from DocQuery
nlp = pipeline('document-question-answering')

def main():
    st.title("PDF Document Question-Answering App")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    question = st.text_input("Ask your question:")

    if st.button("Get Answer"):
        if uploaded_file and question:
            answer = get_answer(uploaded_file, question)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please upload a PDF file and enter a question.")

def get_answer(uploaded_file, question):
    # Fetch the document content from the uploaded file and process the question
    doc = fetch_document(uploaded_file)
    result = nlp(question=question, **doc.context)
    return result

def fetch_document(uploaded_file):
    # In this function, you can process the uploaded PDF file and create a 'Document' object with the content
    # You can use libraries like PyPDF2 or pdfminer to extract text from the PDF file

    # For example, extracting text using PyPDF2
    import PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
    pdf_text = ""
    for page_num in range(pdf_reader.numPages):
        pdf_page = pdf_reader.getPage(page_num)
        pdf_text += pdf_page.extractText()
    
    # For simplicity, here we just create a 'Document' object with the extracted text
    doc = Document(pdf_text)
    return doc

class Document:
    def __init__(self, content):
        self.context = {'text': content}

if __name__ == "__main__":
    main()


# In[ ]:




