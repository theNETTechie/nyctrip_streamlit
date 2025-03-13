import streamlit as st
from common.inputs import input_database_form, input_schema_form, input_table_form
import pandas as pd

# import ptvsd
# ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)

st.title(f"Sample - Select and Display Table")
conn = st.connection("snowflake")
session = conn.session()

# Initialize Session State
if 'input_db' not in st.session_state:
    st.session_state.input_db = None
    st.session_state.input_schema = None
    st.session_state.input_tbl = None
        
input_database_form(session)

if (st.session_state.input_db):
    input_schema_form(session, st.session_state.input_db)
else:
    st.session_state.input_schema = None

if (st.session_state.input_schema):
    input_table_form(session, st.session_state.input_schema)
else:
    st.session_state.input_tbl = None

if (st.session_state.input_tbl):
    data_frame = session.sql(f'SELECT * from {st.session_state.input_tbl}').to_pandas()
    st.write(data_frame.head(10))


