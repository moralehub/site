# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Titulo")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Cabeçalho")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Bugatti Chiron")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR63Xd7XIGAadQMMQxl-9ULgeHaf_WJCN5o4Q&s")
