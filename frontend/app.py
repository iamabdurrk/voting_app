import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Voting System")

candidates = ["Alice", "Bob", "Charlie"]
vote = st.radio("Choose a candidate:", candidates)

if st.button("Submit Vote"):
    response = requests.post(f"{API_URL}/vote/", json={"candidate": vote})
    st.success(response.json()["message"])

if st.button("View Results"):
    response = requests.get(f"{API_URL}/results/")
    st.write(response.json())
