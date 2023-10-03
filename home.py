#en esta parte del codigo se importan las librerias
import streamlit as st
from PIL import Image



#esta parte del codigo genera el titulo y proposito de la app
st.title("¡Bienvenido!")
st.write("Esta aplicación se llama KATOG 3000, lo cual fue creada con el fin de conocer la edad humana de nuestras mascotas, ya que como dueños no sabemos realmente en que etapa están nuestras mascotas.")

#en esta parte del codigo se genera un texto y una imagen con las indicaciones para utilizar la app
st.title("¿Como usarla?")
st.write("Primero que todo deberas seleccionar si tu mascota es un perro o un gato.")
image = Image.open("imagen_2023-09-26_121139623.jpg")
st.image(image, caption='🡱ㅤㅤejemploㅤㅤ🡱')

st.write("Luego de que te salga una foto de la espécie de tu mascota, deberás bajar y hacer click en el botón confirmar. ")
image = Image.open("imagen_2023-09-26_122352288.jpg")
st.image(image, caption='🡱ㅤㅤejemploㅤㅤ🡱')

st.write("Al momento de hacer click verás una tabla con las respectivas edades.")