from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_interface import get_sql_from_question, execute_sql_query

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_PATH = "ecommerce.db"

SCHEMA = """
Table: AdSales
  date (TEXT)
  item_id (INTEGER)
  ad_sales (REAL)
  impressions (INTEGER)
  ad_spend (REAL)
  clicks (INTEGER)
  units_sold (INTEGER)
"""

# Request model
class QuestionRequest(BaseModel):
    question: str

# POST endpoint
@app.post("/ask")
def ask_question(data: QuestionRequest):
    try:
        sql_query = get_sql_from_question(data.question, SCHEMA)
        result = execute_sql_query(DATABASE_PATH, sql_query)
        return {
            "question": data.question,
            "generated_sql": sql_query,
            "results": result
        }
    except Exception as e:
        return {
            "question": data.question,
            "generated_sql": sql_query if 'sql_query' in locals() else "",
            "results": [],
            "error": str(e)
        }
