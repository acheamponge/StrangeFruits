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
    st.sidebar.title("Navigate yourself...")
    menu_selection = st.sidebar.radio("Choice your option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

    st.sidebar.info(
        "https://github.com/acheamponge/american_lynchings"
    )
    

if __name__ == "__main__":
    main()