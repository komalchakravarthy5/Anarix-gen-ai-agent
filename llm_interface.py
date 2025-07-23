import re
import sqlite3
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

# ✅ Load llama3
llm = Ollama(model="llama3")

# ✅ Strict SQL generation prompt
template = """
You are a strict SQL assistant. Given the database schema:

{schema}

Convert the following question into a valid SQL query using only SQLite syntax.

Question: {question}

Only return the SQL query. Do NOT include explanation, markdown, or extra text. Return ONLY the SQL query.
"""

prompt = PromptTemplate(
    input_variables=["schema", "question"],
    template=template
)

# ✅ Runnable chain using LangChain v0.2+
chain = prompt | llm

# ✅ Extract SQL from LLM
def get_sql_from_question(question: str, schema: str) -> str:
    raw_output = chain.invoke({"schema": schema, "question": question}).strip()
    print("🔍 LLM Raw Output:\n", raw_output)

    # Extract just SQL
    match = re.search(r"(SELECT\s.+?;)", raw_output, re.IGNORECASE | re.DOTALL)
    sql = match.group(1).strip() if match else raw_output
    print("✅ Clean SQL Extracted:\n", sql)
    return sql

# ✅ Run SQL query on SQLite
def execute_sql_query(db_path: str, query: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
    finally:
        conn.close()
