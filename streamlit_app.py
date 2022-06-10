import streamlit
import pandas as pd
streamlit.title('Streamlit App')
jobs = pd.read_json('https://jobs.samuelbagattin.com/index.json')
streamlit.dataframe(jobs)