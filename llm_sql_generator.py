from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain.chains.sql_database.query import create_sql_query_chain
from dotenv import load_dotenv

load_dotenv()

def initialize_llm():
    """
    Initialize the Gemini LLM with the provided API key.

    Args:
        api_key (str): Google Generative AI API key.

    Returns:
        ChatGoogleGenerativeAI: An initialized LLM object.
    """

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    return llm


def get_sql_prompt():
    """
    Returns a PromptTemplate for generating SQL from natural language questions.

    Returns:
        PromptTemplate: The formatted SQL prompt template.
    """

    prompt = PromptTemplate(
        input_variables=["input", "top_k", "table_info"],
        template="""
        You are an expert SQL developer with deep knowledge of databases and SQL query optimization. 
        Your task is to generate a syntactically correct SQL query based on a natural language question and the given database schema.
        
        Instructions:
        - Focus on writing clear, efficient SQL queries.
        - Only use the provided tables and columns.
        - Ensure that the query is well-optimized, making use of appropriate filtering, sorting, and joins if necessary.
        - Avoid including unnecessary columns or complex operations unless explicitly requested.
        - The question may contain requests for specific columns, filters, and orderings.
                
        Question: {input}
        Top K: {top_k}
        {table_info}

        SQL Query:
        """
    )
    return prompt


def generate_sql_query(question, db):
    """
    Generates and runs an SQL query from a natural language question.

    Args:
        question (str): The natural language query.
        db (SQLDatabase): The connected SQLDatabase object.
        api_key (str): Google Gemini API key.

    Returns:
        dict: Dictionary with final result and intermediate steps including generated SQL.
    """

    llm = initialize_llm()
    prompt = get_sql_prompt()
    chain = create_sql_query_chain(llm, db, prompt=prompt)

    return chain.invoke({"question": question, "top_k": None})
