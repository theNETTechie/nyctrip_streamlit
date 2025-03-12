import streamlit as st
from snowflake.snowpark import Session
import pandas as pd

def input_database_form(session: Session):
    with st.form("Select_Database"):
        databases_df = session.sql("SHOW DATABASES").collect()
        databases = [database["name"] for database in databases_df]
        input_db = st.selectbox("Enter the Database Name:", databases, index=None, placeholder="Select a database.")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.session_state.input_db = input_db
            st.session_state.input_tbl = None
        

def input_table_form(session: Session, input_db: str): 

    with st.form("Select_Table"):
        tables_df = session.sql(f"SHOW TABLES IN SCHEMA {input_db}.PUBLIC").collect()
        tables = [table["name"] for table in tables_df]

        if len(tables) > 0:
            input_table = st.selectbox("Table:", tables, index=None, placeholder="Select a table.")
            submitted = st.form_submit_button("Submit")

        if submitted:
            st.write(f"Selected table is {input_table}")
            st.session_state.input_tbl = f"{input_db}.PUBLIC.{input_table}"

