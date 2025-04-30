import streamlit as st
import pandas as pd
from sql_handler import connect_to_mysql_database, list_mysql_databases, run_query
from llm_sql_generator import generate_sql_query

st.set_page_config(page_title="AI SQL Agent", layout="wide")
st.title("🤖 Insightforge AI SQL Agent")

# --- SIDEBAR ---
st.sidebar.header("🛠️ MySQL Configuration")
host = st.sidebar.text_input("Host", value="localhost")
port = st.sidebar.number_input("Port", value=3307, step=1)
username = st.sidebar.text_input("Username", value="root")
password = st.sidebar.text_input("Password", type="password")

# Load available databases button
if st.sidebar.button("🔄 Load Databases"):
    try:
        databases = list_mysql_databases(username, password, host, port)
        st.session_state.databases = databases
        st.success("Databases loaded successfully!")
    except Exception as e:
        st.error(f"Error: {e}")

# Dropdown to select DB
db_name = st.sidebar.selectbox("Select Database", st.session_state.get("databases", []))

# Connect button
if st.sidebar.button("🔌 Connect"):
    try:
        db = connect_to_mysql_database(username, password, db_name, host, port)
        st.session_state.db = db
        st.success(f"Connected to `{db_name}` successfully!")
    except Exception as e:
        st.error(f"Connection failed: {e}")

# --- MAIN INTERFACE ---
if "db" in st.session_state:
    db = st.session_state.db

    st.subheader("💬 Ask Your SQL Question")
    question = st.text_input("Type your natural language query", placeholder="e.g. Show me all customers from the USA")

    if st.button("🚀 Run Query") and question:
        try:
            # Step 1: Generate SQL from question
            st.info("Generating SQL query from your question...")
            response = generate_sql_query(question, db)
            sql_query = response.strip().replace("```sql", "").replace("```", "").strip()

            # Step 2: Display SQL Query
            st.code(sql_query, language="sql")

            # Step 3: Execute SQL and show result
            st.info("Running SQL on database...")
            df = run_query(db, sql_query)
            st.success("✅ Query Executed Successfully!")

            # Step 4: Show results as DataFrame
            st.dataframe(df, use_container_width=True)

            # Step 5: Download button
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Results as CSV", csv, "results.csv", "text/csv")

        except Exception as e:
            st.error(f"❌ Error: {e}")

else:
    st.warning("Please connect to a MySQL database to begin.")
