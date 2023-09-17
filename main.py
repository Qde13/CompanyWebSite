import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
description = """CreativeTech Solutions is a dynamic and innovative technology company dedicated to solving complex 
problems through cutting-edge solutions. Established in 2010, we've steadily grown into a trusted partner for 
businesses seeking to harness the power of technology to drive growth and efficiency."""
st.write(description)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv",sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

