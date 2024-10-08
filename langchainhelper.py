from langchain.document_loaders import csv_loader
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI


def createEmbeddings():

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    return embeddings


def createVectorDB(file_path):

    documnet = csv_loader.CSVLoader(file_path="codebasics_faqs.csv",source_column= "prompt",encoding = "latin-1")
    data = documnet.load()

    embeddings = createEmbeddings()
    vectordb = FAISS.from_documents(documents=data, embedding=embeddings)

    vectordb.save_local(file_path)

def get_qa_chain(file_path, llm):
    embeddings = createEmbeddings()
    vectordb = FAISS.load_local(file_path, embeddings,allow_dangerous_deserialization=True)

    retriever = vectordb.as_retriever(threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know. I am specialized in answering question related to codebasics" Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}

   """
    
    prompt = PromptTemplate(
        template = prompt_template,
        input_variables = ["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriever,
        input_key = "query",
        return_source_documents=True,
        chain_type_kwargs = {"prompt":prompt}

    )
    
    return chain

    

