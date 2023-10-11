import streamlit as st
from send_email import contactMe

st.header("Contact Me")

with st.form(key="email_form"):
    userEmail = st.text_input("Enter here your email address")
    raw_message = st.text_area("Enter here your message")
    message = f"""\
Subject: new email from {userEmail}

from: {userEmail}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        contactMe(message)
        st.info("Your email was sent successfully")
