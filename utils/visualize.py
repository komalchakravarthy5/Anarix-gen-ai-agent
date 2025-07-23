import plotly.express as px
import pandas as pd

def create_bar_chart(data: list[dict], x_key: str, y_key: str, filename: str = "chart.png"):
    df = pd.DataFrame(data)
    fig = px.bar(df, x=x_key, y=y_key, title="Auto-generated Chart")
    fig.write_image(filename)
    return filename
