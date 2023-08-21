import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

st.write('''
Data Science Salary Analysis
''')

@st.cache_data()
def load_data():
    return  pd.read_csv('datasets/ds_salaries.csv')

with st.spinner("Loading dataset..."):
    df = load_data()

    st.title('my Datascience App')
    st.dataframe(df)

    st.header('Data Visualization')
    st.subheader('job titles of the employes')
    job_count = df['job_title'].value_counts().head(10)


figl  =  px. bar(job_count,
                 job_count.index,
                 job_count.values,
                 title = 'job title of the employees')
st.plotly_chart(figl, use_container_width=True)
st.subheader("these are the popular jobs")
st.info(",".join(job_count.index.tolist()))
                 