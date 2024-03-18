import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Investment Details by RAM", layout="wide")
st.title('Investment Details')
data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vScwbSgLHpruvFkDdh_QrjcoheKVnPHyUwOkIKcKgU2r6h6t5SGk5qkuJlXDtwuTM50cQMu4OWliZEp/pub?output=csv')

query = st.text_input("Enter Your PAN Number: ")

if query:
    mask = data.applymap(lambda x: query in str(x).lower()).any(axis=1)
    df = data[mask]
    st.write(df)