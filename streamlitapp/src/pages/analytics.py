import pathlib
import utils.display as udisp
import pandas as pd

import streamlit as st


def write():
    udisp.title_awesome("Data Analytics")
    
    with open('../data/lynchings.csv', 'r') as f:
        df = pd.read_csv(f)
    
    st.dataframe(df)