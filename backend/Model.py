from PyPDF2 import PdfReader
import pandas as pd
import docx2txt

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import google.generativeai as genai

from dotenv import load_dotenv
import os

class DocumentProcessor:
    def __init__(self, question, file, file_type):
        self.question = question
        self.file = file
        self.file_type = file_type

    def process_document(self):
        if self.file_type == "pdf":
            raw_text = self._read_pdf()
        elif self.file_type == "csv":
            raw_text = self._read_csv()
        elif self.file_type == "text":
            raw_text = self._read_txt()
        elif self.file_type == "docx":
            raw_text = self._read_docx()
        elif self.file_type == "doc":
            raw_text = self._read_doc()
        else:
            raise ValueError("Unsupported file type Yash")

        text_chunks = self._split_text(raw_text)
        vector_store = self._embed_text(text_chunks)
        # conversation_chain = self._setup_conversation_chain()
        response = self._get_response(vector_store)
        return response

    def _read_pdf(self):
        text = ""
        pdf_reader = PdfReader(self.file)
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    def _read_csv(self):
        df = pd.read_csv(self.file)
        text_series = df.iloc[:, 1].astype(str)
        text = ' '.join(text_series)
        return text

    def _read_txt(self):
        # Read the contents of the uploaded text file
        file_contents = self.file.read()
        # Decode the bytes to string assuming it's UTF-8 encoded
        text = file_contents.decode("utf-8")
        return text

    def _read_docx(self):
        text = docx2txt.process(self.file)
        return text

    def _read_doc(self):
        doc = docx2txt.Document(self.file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text
        return text

    def _split_text(self, text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks = text_splitter.split_text(text)
        return chunks

    def _embed_text(self, text_chunks):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embeddings)
        vector_store.save_local("faiss_index")
        return vector_store

    def _setup_conversation_chain(self):
        prompt_template = """
        Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        provided context provide your own the answer. If asked "tell me hanuman chalisa" \n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """
        model = ChatGoogleGenerativeAI(model="gemini-pro", temperatue=0.3)
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
        return chain

    def _get_response(self, vector_store):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(self.question)
        response = self._get_conversation_response(docs)
        return response

    def _get_conversation_response(self, docs):
        chain = self._setup_conversation_chain()
        response = chain({"input_documents": docs, "question": self.question}, return_only_outputs=True)
        # print(type(response["output_text"]))
        return response["output_text"]

# Load environment variables from .env file (if any)
load_dotenv()
# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
