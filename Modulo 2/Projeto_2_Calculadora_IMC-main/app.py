import streamlit as st


# ----------------------------    --------------------------------------------------------------SIDEBAR

st.sidebar.title("Calculadora de imc !")
st.sidebar.image("logo.png")








#-----------------------------------------------------------------------------------------------BODY

st.title("Calculadora de imc !")

peso = st.text_input("Digite seu peso: ", 0.0)
altura = st.text_input("Digite sua altura: ", 0.0)

if st.button("Calcular"):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)


    if imc < 18.5:
        class_imc = "abaixo_do_peso"

        st.warning(f"Seu imc é {imc:.2f}. Voce está abaixo do peso ")

    elif imc < 24.9:
        class_imc = "peso_saudavel"
        st.success(f"seu imc é {imc:.2f}. Seu peso é saudavel ") 

    elif imc < 29.9:
        class_imc = "sobrepeso"
        st.warning(f"Seu imc é {imc:.2f}.voce esta com sobre peso ")
    
    elif imc < 34.9:
        class_imc = "obesidade_1"
        st.warning(f"Seu imc é {imc:.2f}. Voce esta com obesidade grau 1")

    elif imc < 39.9:
        class_imc = "obesidade_2"
        st.error(f"Seu imc é {imc:.2f}. Voce esta com obesidade grau 2")

    else :
        class_imc = "obesidade_3"
        st.error(f"Seu imc é {imc:.2f}. Voce esta com obesidade grau 3")

    st.markdown("-----")

    st.image(f"{class_imc}.png")

    with open(f"{class_imc}.txt","r", encoding="utf-8") as f:
        texto = f.read()

    st.markdown(texto)