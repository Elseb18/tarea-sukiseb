#en esta parte del codigo se importan las librerias
import streamlit as st
from PIL import Image


st.title("¿Quieres saber que edad tiene tu mascota? (años humanos)")
mascota = st.radio(
        "Escoge tu mascota👇",
        ["Perro", "Gato", "No tengo :("])

if mascota == "Perro":
    image = Image.open("ilustracion-icono-vector-dibujos-animados-hueso-mordedura-perro-pug-lindo-naturaleza-animal-icono-co.jpg")
    st.image(image, caption='U・ᴥ・U')
    if st.button("confirma guau"):
        tabla = Image.open("imagen_2023-09-25_153528724.jpg")
        st.image(tabla, caption='tabla')


    

elif mascota == "Gato":
    image = Image.open("ilustracion-icono-vector-dibujos-animados-lindo-gato-sentado-concepto-icono-naturaleza-animal-aislad.jpg")
    st.image(image, caption='(^･ｪ･^)ฅ')
    if st.button("confirma miau"):
        tabla = Image.open("imagen_2023-09-25_154205709.jpg")
        st.image(tabla, caption='tabla')
        
    

elif mascota == "No tengo :(":
    image = Image.open("2FPVA73ONZHNBJ3SWXVRHHTPGI.jpg")
    st.image(image, caption='esta app no es para ti >:(')



    
