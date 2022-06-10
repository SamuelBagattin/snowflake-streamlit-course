import streamlit
import pandas as pd
import snowflake.connector as conn
streamlit.title('Streamlit App')
my_cnx = conn.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FDC_FOOD_INGEST")

my_data_row = my_cur.fetchall()

streamlit.text("Hello from Snowflake:")

streamlit.dataframe(my_data_row)