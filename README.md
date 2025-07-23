## GenAI SQL Agent

An AI-powered agent that converts natural language questions into SQL queries, executes them on a local SQLite database, and returns results via a FastAPI backend. Includes a simple web frontend for interactive querying.

---

### Features

- **Natural Language to SQL**: Uses LLM (Llama3 via Ollama) to convert user questions into SQL queries.
- **SQLite Database**: Works with a sample e-commerce database (`ecommerce.db`) built from CSV datasets.
- **FastAPI Backend**: Exposes a `/ask` endpoint for question answering.
- **Web Frontend**: Simple HTML interface for asking questions and viewing results.
- **Data Visualization**: Utilities for generating charts from query results (see `utils/visualize.py`).

---

### Project Structure

```
├── datasets_to_sql.py      # Script to load CSVs into SQLite
├── ecommerce.db            # SQLite database (auto-generated)
├── index.html              # Web frontend
├── inspect_db.py           # Inspect DB schema/tables
├── llm_interface.py        # LLM prompt & SQL generation logic
├── main_api.py             # FastAPI backend
├── requirements.txt        # Python dependencies
├── sql_handler.py          # SQL execution & schema extraction
├── utils/
│   └── visualize.py        # Chart generation utility
└── datasets/
    ├── Ad_Sales.csv
    ├── Eligibility.csv
    └── Total_sales.csv
```

---

### Setup & Installation

1. **Clone the repository**
2. **Install Python dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Install and run Ollama**
   - Download from [ollama.com](https://ollama.com/)
   - Pull the Llama3 model:
     ```
     ollama pull llama3
     ```
   - Ensure Ollama is running locally.
4. **Prepare the database**
   ```
   python datasets_to_sql.py
   ```
5. **Start the FastAPI server**
   ```
   uvicorn main_api:app --reload
   ```
6. **Open the frontend**
   - Open `index.html` in your browser.

---

### Usage

1. Enter a natural language question (e.g., "What is the total ad spend?") in the web UI.
2. The backend generates SQL, executes it, and returns results.
3. Results and the generated SQL are displayed in the browser.

---

### Tech Stack

- Python, FastAPI, Pydantic
- LangChain, Ollama (Llama3)
- SQLite, Pandas
- Plotly (for visualization)
- HTML/CSS/JS (frontend)

---

### Example Questions

- What is the total ad spend?
- Show all items with impressions greater than 1000.
- List units sold by date.

---

### Notes

- The LLM is prompted to return only valid SQLite SQL queries.
- You can inspect or modify the database schema using `inspect_db.py`.
- For custom visualizations, use `utils/visualize.py`.

---

### License

MIT
