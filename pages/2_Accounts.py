import streamlit as st


st.set_page_config(page_title="Accounts", layout="wide")

if st.session_state.logged_in:
    st.header('Accounts')
    st.subheader('Net Income')
    st.write('Assets vs Debts')
    st.subheader('Credit Cards')
    st.subheader('Depository')