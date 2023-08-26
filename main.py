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
st.markdown('''
## what can we find out?
            -year
            -experience
            -employement type
            -job title
            -location
            company size
            -currency
- statistical analysis of diffrent category vs salary
   ''')   
categories = df.select_dtypes(exclude=np.number).columns .tolist()    
st.success(f'There are following categories: {",".join(categories)}')   
for col in categories:
    counts = df[col].value_counts()
    if df[col].nunique()> 10:
        fig = px.bar(counts,
                     counts.index,
                     counts.values,
                     log_y=True,
                     title = f'Distrubution of {col}')
        fig.update_traces(texttemplate='%{text:.2s}', textposition= 'outside')
    else:
        fig  = px.pie(counts,
                      counts.index,
                      counts.values,
                
                     title = f'Distrubution of {col}')
    st.plotly_chart(fig, use_container_width=True)

year_wise_df_sum = df.groupby('work_year')[['salary' ,'salary_in_usd']].sum().reset_index()
year_wise_df_mean = df.groupby('work_year')[['salary' ,'salary_in_usd']].mean().reset_index()
st.dataframe(year_wise_df_sum, use_container_width=True) 

fig = px.bar(year_wise_df_sum,
               'work_year','salary_in-usd',
               title='salary trend over the years' )    
fig2 = px.area(year_wise_df_mean,
               'work_year','salary_in-usd',
               title='mean salary trend over the years' )    
c1,c2 =st.column(2)
c1.plotly_chart(fig,use_container_with=True)
c2.plotly_chart(fig2,use_container_with=True)


    



           



                 