import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact me")

with st.form(key="email_forms"):
    email = st.text_input("Your email address:")
    select_box = st.selectbox(
        "What topic do uou want to discuss?:",
        df["topic"])
    message_area = st.text_area("Write your message here:")

    message = f"""\
Subject: New email from {email}
    
From:{email}
Topic {select_box}
{message_area}
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Message sent successfully!")

