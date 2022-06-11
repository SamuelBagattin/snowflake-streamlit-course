import numpy
import pandas
import streamlit
import pandas as pd
import numpy as np

streamlit.title('Jobs')


def get_all_technologies(companies_local):
    technologies = []
    for company in companies_local:
        technologies.append(company['MainTechnologies'])
    return set(np.concatenate(numpy.array(technologies, dtype=object).flatten()).ravel())


data = pd.read_json('https://jobs.samuelbagattin.com/index.json')
companies = data['Companies']['Companies']
technologies = get_all_technologies(companies)

chosen_technologies = streamlit.multiselect('Filter by technology', technologies, default=[])
filtered_companies = [company for company in companies if
                      all(technology in company['MainTechnologies'] for technology in chosen_technologies)]

companies_df = pandas.DataFrame(filtered_companies, columns=['CompanyName', 'MainTechnologies'])
streamlit.dataframe(companies_df)
