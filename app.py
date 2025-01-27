import streamlit as st
from pymatgen.core import Composition

# Configuración de la página
st.set_page_config(
    page_title="Cálculo de Peso Molecular",
    page_icon="🧪",
    layout="centered",
)

# Título y descripción
st.title("🧪 Calculadora de Peso Molecular")
st.subheader("De fórmula química a masa molecular ⚗️")
st.write("Introduce una fórmula química para calcular su peso molecular (en gramos/mol).")

# Entrada del usuario
formula = st.text_input("Fórmula química (Ejemplo:
