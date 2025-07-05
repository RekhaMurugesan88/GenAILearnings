import streamlit as st
st.title("my first streamlit app")
name = st.text_input("Enter your name")

if st.button("say hello"):
    if name:
        st.success(f"hello {name}, Welcome to my page")
    else:
        st.warning("Please enter your name")