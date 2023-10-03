import streamlit as st
from PIL import Image


st.title("Esta app fue creada por:")
st.title("Fernanda Barbé y Sebastián Castillo")
st.title("DEL 4TO BLUE.")


image = Image.open("download20231001145808.jpg")



image = Image.open("download20231001150602.jpg")



col1, col2, = st.columns(2)

with col1:
   st.header("suki")
   st.image("download20231001145808.jpg")

with col2:
   st.header("seb")
   st.image("download20231001150602.jpg")
