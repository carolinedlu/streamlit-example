import streamlit as st
import base64

href = f'<a href="/files/example.xlsx" download="example.xlsx">Download XLSX File</a>'
st.markdown(href, unsafe_allow_html=True)
