import streamlit as st
from common.hello import say_hello
from common.inputs import input_database_form, input_table_form
import pandas as pd

# import ptvsd
# ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)

st.title(f"Sample - Select and Display Table")
conn = st.connection("snowflake")
session = conn.session()

if 'input_db' not in st.session_state:
    st.session_state.input_db = None

if 'input_tbl' not in st.session_state:
    st.session_state.input_tbl = None
        
input_database_form(session)

if (st.session_state.input_db):
    input_table_form(session, st.session_state.input_db)

if (st.session_state.input_tbl):
    data_frame = session.sql(f'SELECT * from {st.session_state.input_tbl}').to_pandas()
    st.write(data_frame.head(5))


