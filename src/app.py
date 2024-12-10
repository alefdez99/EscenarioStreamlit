import streamlit as st

st.title("Suma de valores")

num1 = st.number_input("Introduzca primer valor")
num2 = st.number_input("Introduzca segundo valor")

sum = num1 + num2

if sum:
    st.write(f"La suma de {num1} y {num2} es {sum}")