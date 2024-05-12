import arxiv
import os


class Arxiv(object):
    def __init__(self):
        self.__QUERY = ''
        self.__client = arxiv.Client()
        self.__results = []

    def find_papers_by_query(self, QUERY: str) -> None:
        arxiv_search_engine = arxiv.Search(
            query=QUERY,
            max_results=3,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        self.__results = self.__client.results(arxiv_search_engine)

    def save_results_to_pdf_files(self, FOLDER: str):
        RES_FOLDER_NAME: str = f"arxiv/{FOLDER}/papers"
        if not os.path.isdir(RES_FOLDER_NAME):
            os.makedirs(RES_FOLDER_NAME)
        [result.download_pdf(dirpath=RES_FOLDER_NAME, filename=f"{result.title}.pdf") for result in self.__results]
