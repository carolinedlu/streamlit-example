import streamlit as st
import base64

filename=open('example.xlsx', encoding='utf8', errors='ignore')
contents=filename.read().encode()
b64 = base64.b64encode(contents).decode()
href = f'<a href="data:file/xlsx;base64,{b64}" download="file.xlsx">Download XLSX File</a>'
st.markdown(href, unsafe_allow_html=True)
