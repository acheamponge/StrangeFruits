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
    'Offense',
    'Sex'    
            }
    pick_grp = st.selectbox("Groupby: ", list(group))
    
    df3 = df.groupby(pick_grp).count()
    
    df3 = df3[['Victim']]
    df3.columns = ['Count']
    
    st.dataframe(df3)
    
    month_to_filter = st.slider('Filter Data By Month', 0, 12, 8)
    filtered_data_mon = df[df['Month'] == str(month_to_filter)]
    st.dataframe(filtered_data_mon)
    
    year_to_filter = st.slider('Filter Data By Year', 1882, 1930, 1900)
    filtered_data_yr = df[df['Year'] == str(year_to_filter)]
    st.dataframe(filtered_data_yr)
    
    
    states = {
    'AL',
    'AR',
    'FL',
    'GA',
    'KY',
    'LA',
    'MS',
    'NC',
    'SC',
    'TN'
            }
            
    pick_st = st.selectbox("Filter By State: ", list(states))
    filtered_data_st = df[df['State'] == str(pick_st)]
    st.dataframe(filtered_data_st)
    
    
    race = {
    'Blk',
    'Other',
    'Unk',
    'Wht'
            }
            
    pick_rc = st.selectbox("Filter By Race: ", list(race))
    filtered_data_rc = df[df['Race'] == str(pick_rc)]
    st.dataframe(filtered_data_rc)
    
    
    sex = {
    'Male',
    'Fe',
    'Unk'
            }
            
    pick_sex = st.selectbox("Filter By Sex: ", list(sex))
    filtered_data_sex = df[df['Sex'] == str(pick_sex)]
    st.dataframe(filtered_data_sex)