import requests
import streamlit as st
from Database import Database
from Prompt import Prompt
import os


database = Database()
prompt = Prompt()


class Client(object):
    def __init__(self):
        self.__RESPONSE = r'n\a'
        self.__run_streamlit()

    def __ask_llm_with_db(self, LLM: str, PROMPT: str) -> None:
        self.__RESPONSE: str = requests.post(
            f"http://localhost:8001/{LLM}/invoke",
            json={"input": {"input": PROMPT}}
        ).json()["output"]

    def __run_streamlit(self):
        st.title("Langchain Demo with API")
        QUERY: str = st.text_input("Ask about...", key="prompt")

        database.query = QUERY

        if QUERY == '':
            st.write("nothing has been inputted yet")
        else:
            st.write(f"you inputted: {QUERY}")
            DOWNLOADED_QUERIES: list = os.listdir(path="./arxiv")
            if QUERY.lower() not in DOWNLOADED_QUERIES:
                st.write(f"{QUERY} has not yet been searched on arxiv.org")
                st.write(f"looking for papers on {QUERY} on arxiv.org")
                database.find_papers_by_query_from_arxiv()
                st.write(f"saving results to cache")
                database.save_results_to_arxiv_pdf_files()
                st.write(f"converting results to database:")
                database.convert_papers_to_database()
            else:
                st.write(f"{QUERY} has already been searched on arxiv.org")

            st.write(f"asking llama3: {QUERY}")
            self.__ask_llm_with_db(PROMPT=QUERY, LLM="llama3")
            st.write(f"response llama3: {self.__RESPONSE}")


if __name__ == "__main__":
    client = Client()
