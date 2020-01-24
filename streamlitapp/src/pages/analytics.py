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

    
    df = pd.read_csv(pick, encoding='utf8')
    st.dataframe(df)
    
    
    group = {
    'State',
    'Year',
    'Mo',
    'Race',
    'County',
    'Offense'    
            }
    pick_grp = st.selectbox("Groupby: ", list(group))
    
    df3 = df.groupby(pick_grp).count()
    
    st.dataframe(df3)