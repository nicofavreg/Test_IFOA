import streamlit as st

def main():
    st.title("Ciao a tutti")
    st.header("questa è la mia creazione di un'applicazione")
    if st.button('prova a cliccare'):
        st.title("hai superato la prova, bravo!!")
        st.balloons()
        st.image('lempuyang.jpg')
    st.slider('test slider', 1, 10, 5)

if __name__ == "__main__":
    main()