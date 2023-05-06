import streamlit as st
from streamlit.components.v1 import html

def plaid_link(callback):
    component_value = html(
        open("plaid_link.html").read(),
        height=50,
        events={"message": True},
        key="plaid_link",
    )

    if component_value is not None and "public_token" in component_value:
        public_token = component_value["public_token"]
        callback(public_token)
