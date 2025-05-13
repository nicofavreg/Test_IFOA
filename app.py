import streamlit as st

def main():
    st.title("Ciao a tutti")
    st.header("questa è la mia creazione di un'applicazione")
    if st.button('prova a cliccare'):
        st.text("hai superato la prova, bravo!!")
        st.balloons()

if __name__ == "__main__":
    main()