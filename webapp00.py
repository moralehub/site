# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("UniConstruction | Requisições")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Materiais")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("")

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Bloco estrutural 14 x 19 x 29cm")
    st.image("https://res.cloudinary.com/glide/image/fetch/f_auto,w_500,c_limit/https%3A%2F%2Fpavibloco.com.br%2Fwp-content%2Fuploads%2F2018%2F01%2FF29-L14-Bloco-Desenho-t%25C3%25A9cnico-1.jpg")

with col2:
    st.header("carro da lenda")
    st.image(""
