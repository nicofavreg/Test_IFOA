import streamlit as st

def main():
    st.title("Ciao a tutti")
    st.header("questa è la creazione di un'applicazione")
    if st.button('prova a cliccare'):
        st.title("hai superato il test, bravo!!")
        st.balloons()
        st.image('lempuyang.jpg')

if __name__ == "__main__":
    main()