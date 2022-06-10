import streamlit
import pandas as pd
import snowflake.connector as conn
streamlit.title('Streamlit App')
my_cnx = conn.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_data_row = my_cur.fetchall()

streamlit.text("Hello from Snowflake:")

streamlit.dataframe(my_data_row)