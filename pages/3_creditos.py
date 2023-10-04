#en esta parte del codigo de importan las librerias
import streamlit as st
from PIL import Image

#en esta parte del codigo muestra texto en pantalla
st.title("Esta app fue creada por:")
st.title("Fernanda Barbé y Sebastián Castillo")
st.title("DEL 4TO BLUE.")

#con esta parte se muestran las imagenes
image = Image.open("download20231001145808.jpg")



image = Image.open("download20231001150602.jpg")


# con esta parte ordenamos las imagenes en columnas
col1, col2, = st.columns(2)

with col1:
   st.header("suki")
   st.image("download20231001145808.jpg")

with col2:
   st.header("seb")
   st.image("download20231001150602.jpg")
