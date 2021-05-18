import streamlit as st
import base64

filename=open('example.xlsx')
href = f'<a href="data:file/xlsx" download="example.xlsx">Download XLSX File</a>'
st.markdown(href, unsafe_allow_html=True)
