from VectorDatabase import VectorDatabase
from Arxiv import Arxiv
from Prompt import Prompt


prompt: Prompt = Prompt()
vector_database: VectorDatabase = VectorDatabase()
arxiv: Arxiv = Arxiv()


class Database(object):
    def __init__(self):
        self.__QUERY = ''

    @property
    def query(self):
        return self.__QUERY

    @query.setter
    def query(self, QUERY: str):
        self.__QUERY: str = QUERY

    def find_papers_by_query_from_arxiv(self):
        arxiv.find_papers_by_query(QUERY=self.__QUERY)

    @staticmethod
    def save_results_to_arxiv_pdf_files():
        arxiv.save_results_to_pdf_files(FOLDER="temp")

    @staticmethod
    def convert_papers_to_database():
        vector_database.create_database()
