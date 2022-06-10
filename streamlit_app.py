import streamlit
import pandas as pd
streamlit.title('Streamlit App')
jobs = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(jobs)