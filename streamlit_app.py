import streamlit as st
import pandas as pd
import base64
import io

df = pd.DataFrame(data, columns=["Col1", "Col2", "Col3"])

excel_path = 'test.xlsx'
xlsx = df.to_excel(excel_path)

data = open(excel_path, 'rb').read()
b64 = base64.b64encode(data).decode('UTF-8')
linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="myfilename.xlsx">Download excel file</a>'
st.markdown(linko, unsafe_allow_html=True)
