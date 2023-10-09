import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.PNG", width=400)

with col2:
    st.title("José A. Santiago Molina")
    content="""As a Software Developer in transition, 
    I offer a unique blend of administration knowledge 
    and software development skills. With over 9 years 
    of experience in modelling and implementing 
    processes and instruments for management decision-making,
    I have transitioned into software development, gaining 
    expertise in web technologies like HTML, CSS, JavaScript
    and Phyton.
    """
    st.info(content)

contactmeMessage = """
Below you can find some pf the apps i have built in Python. feel free to contact me.
"""

st.write(contactmeMessage)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])