import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///pollution.db")

df = pd.read_sql("SELECT * FROM pollution", engine)

st.title("Lahore Pollution Dashboard")

st.line_chart(df["pm2_5"])

st.line_chart(df["aqi"])