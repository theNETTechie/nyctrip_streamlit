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
        
def input_schema_form(session: Session, input_db: str):
    with st.form("Select_Schema"):
        schemas_df = session.sql(f"SHOW SCHEMAS IN DATABASE {input_db}").collect()
        schemas = [schema["name"] for schema in schemas_df]

        if len(schemas) > 0:
            input_schema = st.selectbox("Schema:", schemas, index=None, placeholder="Select a schema.")
            submitted = st.form_submit_button("Submit")
        else:
            submitted = False

        if submitted:
            st.write(f"Selected schema is {input_schema}")
            st.session_state.input_schema = f"{input_db}.{input_schema}"

def input_table_form(session: Session, input_schema: str): 
    with st.form("Select_Table"):
        tables_df = session.sql(f"SHOW TABLES IN SCHEMA {input_schema}").collect()
        tables = [table["name"] for table in tables_df]

        if len(tables) > 0:
            input_table = st.selectbox("Table:", tables, index=None, placeholder="Select a table.")
            submitted = st.form_submit_button("Submit")
        else:
            submitted = False

        if submitted:
            st.write(f"Selected table is {input_table}")
            st.session_state.input_tbl = f"{input_schema}.{input_table}"

