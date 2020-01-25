import pathlib
import utils.display as udisp
from PIL import Image
import streamlit as st


def write():
    udisp.title_awesome("Historical American Lynchings")
    image = Image.open('./img/1.jpg')

    st.image(image, use_column_width=True)
    
    st.write(
            """
The Strange Fruits project is data analytics and visualization project that seeks to bring more insights into Historical American Lynchings.

This project provides
- **Data Analytics** of the HAL Project Lynching Dataset.
- **Data Visualization** of the various attributes of the dataset. 
- **Resources** on Lynchings in America.
    """
        )
    st.write(
        f'<iframe width="560" height="315" src="https://www.youtube.com/embed/cvwlPKCfkIM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )
