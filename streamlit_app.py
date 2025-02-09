import streamlit as st
from pygbif import species, occurrences
import random
import kagglehub
import os
import informacion

if "nombre" not in st.session_state:
    st.session_state.nombre="pingüino"

descripcion = informacion.animales[st.session_state.nombre]["descripcion"]
foto = informacion.animales[st.session_state.nombre]["foto"]
paises=informacion.animales[st.session_state.nombre]["paises"]
coordenadas=informacion.animales[st.session_state.nombre]["coordenadas"]

st.title("Animales")
st.header(st.session_state.nombre)
columna1,columna2=st.columns(2)
with columna1:
    st.image(foto,use_container_width=True,caption=st.session_state.nombre)
with columna2:
    st.write("**Descripcion:** " + descripcion)
    for index,columna in enumerate(st.columns(len(paises))):
        pais=paises[index]
        with columna:
            st.image(informacion.banderas[pais],caption=pais)            
    st.map(coordenadas,zoom=0,size=1000000,use_container_width=True,height=300)
for index, boton in enumerate(st.columns(len(informacion.animales))):
    animal=list(informacion.animales.keys())[index]
    with boton:
        if st.button(animal,use_container_width=True):
            st.session_state.nombre= animal
            st.rerun()