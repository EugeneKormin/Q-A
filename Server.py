from flask import Flask, request
from flask_cors import CORS
import asyncio
from flask_socketio import SocketIO, emit
from Prompt import Prompt
from langchain_community.llms import Ollama


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
prompt: Prompt = Prompt()


@app.route('/')
def index() -> str:
    return "index page"


async def get_llama3_response(PROMPT: str) -> str:
  llama3 = Ollama(model="llama3")
  chain = prompt.prompt | llama3
  RESPONSE = chain.invoke(input={"input": PROMPT})
  return RESPONSE


@app.route('/get_response', methods=['GET', 'POST', 'OPTIONS'])
def handle_post_request_from_llama() -> dict:
    if request.method == 'OPTIONS':
        # Handle the preflight OPTIONS request
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET' 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return headers

    # Get the JSON data
    PROMPT: str = request.get_json()["prompt"]

    llama_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(llama_loop)
    RESPONSE: str = llama_loop.run_until_complete(get_llama3_response(PROMPT))
    return {"response_from_server": RESPONSE}


@socketio.on('get_response')
async def handle_post_request_from_llama(message) -> None:
      RESPONSE = await get_llama3_response(PROMPT=message["prompt"])
      emit('llama3_response', {'response': RESPONSE})


if __name__ == '__main__':
    app.run(debug=True)
