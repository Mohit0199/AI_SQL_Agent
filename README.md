# AI-Based SQL Query Generator

An intelligent, AI-driven application that allows users to **query their SQL database using plain English**. This project uses **Google Gemini's large language model (LLM)** and **LangChain** to translate natural language into precise SQL queries, making database access more intuitive and accessible for everyone.

---

## Project Overview

This project is an AI-powered SQL query generator that allows users to interact with their SQL databases using natural language queries. Leveraging the power of Google Gemini's large language model (LLM) through LangChain, the application translates user questions into syntactically correct SQL queries, executes them on the connected database, and returns the results as a Pandas DataFrame — which can also be downloaded as a CSV file for further analysis.

The project includes a user-friendly interface built with Streamlit, enabling easy interaction and visualization of query results. It is designed to work robustly with MySQL databases using SQLAlchemy and LangChain's SQLDatabase utilities.

## Features

- Natural language to SQL query generation using Google Gemini LLM.
- Integration with MySQL databases for executing generated SQL queries.
- Dynamic prompt templates to ensure accurate and context-aware SQL generation.
- Streamlit-based web interface for easy user interaction.
- Supports complex queries with schema awareness.
- Intermediate step outputs for transparency in query generation.
- Robust database connection management using SQLAlchemy.

## Technologies Used

- **Google Gemini**: State-of-the-art generative AI model for natural language understanding and generation.
- **LangChain**: Framework for building applications with LLMs, used here for chaining LLM with SQL database operations.
- **Streamlit**: Python library for building interactive web apps for data science and machine learning.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for database connections.
- **langchain_community.utilities.SQLDatabase**: Utility for connecting and interacting with SQL databases in LangChain.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd sql_ai_agent
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:

   - Create a `.env` file in the project root.
   - Add your Google Gemini API key and any other necessary credentials.

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Use the web interface to enter natural language queries. The app will generate the corresponding SQL query, execute it on your database, and display the results.

## Project Structure

- `llm_sql_generator.py`: Contains logic for initializing the Gemini LLM, creating prompt templates, and generating SQL queries from natural language.
- `sql_handler.py`: Manages database connections and query execution using SQLAlchemy and LangChain's SQLDatabase.
- `app.py`: Streamlit application providing the user interface.

---

This project demonstrates the power of combining modern AI language models with traditional database querying, making data access more intuitive and accessible.
