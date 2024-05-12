from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import os
# import streamlit as st
from pinecone import Pinecone, ServerlessSpec
from pinecone.core.client.exceptions import PineconeApiException


pc = Pinecone(api_key='0b380720-2665-404c-a30b-902f1a575be6')


class VectorDatabase(object):
    def __init__(self):
        self.__FILE: str = ''
        self.__files = os.listdir(path=f"./arxiv/temp/papers")
        self.__FULL_PATH_TO_FILE: str = ""

        self.__retriever_dict = {}
        self.__ID = 0

    def __create_remote_pinecone_index(self):
        pc.create_index(
            name=f"temp",
            dimension=4096,
            metric="cosine",
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )

    def __create_vector_store(self):
        self.__create_remote_pinecone_index() if "temp" not in pc.list_indexes().names() else ...

        index = pc.Index("temp")

        loader = PyPDFLoader(self.__FULL_PATH_TO_FILE)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)

        for doc in docs:
            print(f"{round(((self.__ID+1)/len(docs))*100, 3)}%")
            vector: dict = {
                "id": f"vec{self.__ID}",
                "values": OllamaEmbeddings().embed_query(doc.page_content),
                "metadata": {
                    "source": doc.metadata["source"].split('papers/')[1].replace('.pdf', ''),
                    "page": doc.metadata["page"]
                }
            }
            index.upsert(vectors=[vector], namespace=f"ns")
            self.__ID += 1

    def create_database(self):
        for INDEX, self.__FILE in enumerate(self.__files):
            self.__FULL_PATH_TO_FILE: str = f"./arxiv/temp/papers/{self.__FILE}"
            print(f"[{INDEX+1} of {len(self.__files)}]. {self.__FILE.replace('.pdf', '')}")
            # st.write(f"[{INDEX+1} of {len(files)}]. {COLLECTION_NAME}")
            self.__create_vector_store()

            try:
                self.__create_remote_pinecone_index()
            except PineconeApiException:
                pass
