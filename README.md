# Arxiv Paper Retrieval System (In Progress)

This is a work-in-progress project that aims to create a system for retrieving research papers from the arXiv repository based on user queries. The system will allow users to input a query, fetch relevant papers from arXiv, and store them in a vector database for efficient retrieval and analysis.

## Current Progress

The project is currently under active development, and the codebase includes the following files:

- `Arxiv.py`: This file contains a class for interacting with the arXiv API, querying for papers, and downloading them as PDF files.
- `Database.py`: This file serves as a central hub for managing the interaction between different components, such as fetching papers from arXiv and converting them to a vector database.
- `Prompt.py`: This file defines a prompt template for a language model that can be used to generate responses based on the retrieved papers and user queries.
- `Server.py`: This file sets up a gRPC server for handling incoming requests to fetch papers from arXiv and generate responses.
- `VectorDatabase.py`: This file contains a class for creating a vector database using the Pinecone vector database service. It loads the downloaded PDF files, splits them into chunks, embeds the chunks using a language model, and stores them in the Pinecone database.

## Planned Features

The following features are planned for future updates:

- **User Interface**: Develop a user-friendly interface (e.g., a web application or command-line interface) for users to input their queries and receive responses.
- **Query Processing**: Implement logic to process user queries, fetch relevant papers from arXiv, and store them in the vector database.
- **Paper Analysis**: Integrate the language model prompt for analyzing the retrieved papers, generating summaries, and providing relevant information based on the user's query.
- **Database Management**: Enhance database management capabilities, including indexing, updating, and querying the vector database efficiently.
- **Error Handling and Logging**: Implement robust error handling and logging mechanisms to ensure a stable and reliable system.
- **Deployment and Scaling**: Prepare the system for deployment and scaling to handle larger volumes of data and user requests.

## Contributing

As this project is still in progress, contributions are welcome! If you are interested in contributing or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
