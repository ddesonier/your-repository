import streamlit as st
import os
from streamlit_msal import Msal
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
tenant_id = os.getenv('tenant_id')

auth_data = Msal.initialize(
    client_id=client_id,
    authority=f"https://login.microsoftonline.com/{tenant_id}",
    scopes=["User.Read"]
)

if st.button("Sign in"):
    Msal.sign_in()

if auth_data:
    st.write("Success You are signed in")
    st.json(auth_data)
else:
    st.write("You are not signed in")
if st.button("Sign out"):
    Msal.sign_out()
    st.write("You have signed out")