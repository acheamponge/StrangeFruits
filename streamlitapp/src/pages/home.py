import pathlib
import utils.display as udisp

import streamlit as st


def write():
    udisp.title_awesome("Strange Fruits Project")
 
    st.write(
        f'<iframe width="560" height="315" src="https://www.youtube.com/embed/cvwlPKCfkIM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )
