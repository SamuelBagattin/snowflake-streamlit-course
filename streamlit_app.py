import streamlit
import pandas as pd
streamlit.title('Streamlit App')
jobs = pd.read_json('jobs.samuelbagattin.com/index.json')
streamlit.dataframe(jobs)