from fastapi import FastAPI
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
from Database import Database
from Prompt import Prompt


prompt: Prompt = Prompt()
database: Database = Database()


class API(object):
    def __init__(self):
        self.__app = FastAPI(
            title="Langchain Server",
            version="0.1",
            description="A simple RAG API server"
        )

        add_routes(
            self.__app,
            prompt.enhance_with_context(marker=__name__) | Ollama(model="llama3"),
            path="/llama3"
        )

        self.__run()

    def __run(self):
        uvicorn.run(self.__app, port=8001)


if __name__ == "__main__":
    api = API()
