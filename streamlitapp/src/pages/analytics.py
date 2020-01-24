import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st


def write():
    udisp.title_awesome("Data Analytics")
    
    
    keys = {
    '../data/lynchings.csv'
            }
            
    pick = st.selectbox("Select Dataset: ", list(keys))
    
    
    analysis = {
    'count'
            }
            
    
    df = pd.read_csv(pick, encoding='utf8')
    
    

    
    
    df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
    st.dataframe(df)
    
    ana = st.selectbox("Select Aggregation: ", list(analysis))
    
    if ana=='count':
        st.info("Total Number of Lynchings: " + str(df.shape[0]))
    
    group = {
    'State',
    'Year',
    'Month',
    'Race',
    'County',
    'Offense'    
            }
    pick_grp = st.selectbox("Groupby: ", list(group))
    
    df3 = df.groupby(pick_grp).count()
    
    df3 = df3[['Victim']]
    df3.columns = ['Count']
    
    st.dataframe(df3)