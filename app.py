import streamlit as st

# Change title of the app from configs
st.set_page_config(
    page_title="Hello, Streamlit!",
    page_icon="👋",
)

title = st.secrets["title"]

st.title()
