from langchain_core.prompts import ChatPromptTemplate
# from VectorDatabase import VectorDatabase


# vector_database = VectorDatabase()


class Prompt(object):
    def __init__(self):
        pass

    @property
    def prompt(self) -> ChatPromptTemplate:
        TEMPLATE = """
            Task:

            Context Analysis: Thoroughly examine the provided context documents (text, code, data, etc.) to extract key concepts, findings, and limitations.
            User Intent Recognition: Analyze the user's question to understand their specific goals and the information they seek.
            Context Integration: Leverage the knowledge gained from the context analysis to answer the user's question in a comprehensive and informative way.
            Transparency about Limitations: Be transparent about any limitations in the provided context or your own capabilities. If specific information is missing, acknowledge it and suggest potential solutions (e.g., consulting original sources).
            Knowledge Integration (Optional): If past analyses or related information are available, consider incorporating those insights to enrich your response, ensuring their relevance to the user's question.
            
            Output:
            Do not add task and considerations to response.
            Generate a well-structured (from point of view of string formatting) answer that directly addresses the user's question.
            Clearly explain concepts using language appropriate for the user's level of understanding.
            Cite sources when referencing information from the context documents.
            Crucial Considerations:
            
            Focus on Evidence-Based Response: Base your answer on the factual information present in the context documents. Avoid making claims that are not directly supported by the evidence.
            Highlight Uncertainties: If the context lacks specific details or there are conflicting findings, acknowledge these uncertainties and suggest potential next steps (e.g., further research).
            Prioritize User Need: Strive to provide the most relevant and helpful information to the user, even if the answer is not complete.
                        
            <Question>
            Question to answer: {input}
            </Question>
        """

        return ChatPromptTemplate.from_template(
            template=TEMPLATE
        )
