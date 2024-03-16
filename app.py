import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("My Streamlit Weather App")

st.header("Weather Data", divider="blue")

col1, col2, col3, = st.columns(3)
col1.metric("Temperature", 70, f"{5}%")
col2.metric("Precipitation - Rain" , .5,  f"{-2}%")
col3.metric("Humidity" , 52.5 , f"{20}%")

data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100)
})

df = pd.DataFrame(data)

st.subheader("Line Chart", divider="blue")

st.line_chart (df)

