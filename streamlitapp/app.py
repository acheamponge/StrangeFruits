import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.about
import src.pages.analytics
import src.pages.visualization
import src.pages.resources

MENU = {
    "Home" : src.pages.home,
    "Data Analytics" : src.pages.analytics,
    "Data Visualizations" : src.pages.visualization,
    "Resources" : src.pages.resources,
    "About" : src.pages.about
}

def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Pick an option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

    st.sidebar.title("Contribute")
    st.sidebar.info(
        "This an open source project and please feel free to contribute"
        +"\n"+
        "[Github](https://github.com/acheamponge/historical_american_lynchings)"
        +"\n"+
        "\n"+
        "[Google Docs](https://lnkd.in/eZgNRy6) "
    )
    
      
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This purpose of this app is to create an interactive platform to analyze the dataset of lynchings that happened in America."""
    )
    
    st.sidebar.title("Special Thanks")
    st.sidebar.info(
        "Huge thank you to MarcSkovMadsen and Avkash whose use of Streamlit helped make the webapp for this project"
        +"\n"+
        "[MarcSkovMadsen](https://github.com/MarcSkovMadsen/awesome-streamlit/)"
        +"\n"+"\n"+
        "[Avkash](https://github.com/Avkash/demoapps) "
        )

if __name__ == "__main__":
    main()