import streamlit as st
import pandas as pd
import base64
import io

b64 = base64.b64encode(data).decode('UTF-8')
href = f'<a href="data:file/xlsx;base64,{b64}" download="example.xlsx">Download xlsx File</a>'
st.markdown(href, unsafe_allow_html=True)
