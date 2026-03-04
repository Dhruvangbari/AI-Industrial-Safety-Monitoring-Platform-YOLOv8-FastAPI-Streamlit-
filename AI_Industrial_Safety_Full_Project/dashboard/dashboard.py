
import streamlit as st
import pandas as pd

st.title("Industrial Safety Dashboard")

try:
    df=pd.read_csv("../logs/violations.csv")
    st.dataframe(df)
    if "timestamp" in df.columns:
        st.line_chart(df["timestamp"])
except:
    st.write("No violations yet.")
