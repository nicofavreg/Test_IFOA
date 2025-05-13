import streamlit as st

def main():
    st.title("Ciao a tutti")
    st.header("questa è la creazione di applicazione")
    st.camera_input('take a photo with me')
    st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vacanzeabali.it%2Ftempli%2Ftempio-lempuyang%2F&psig=AOvVaw3laoIFFCPD9jJWv-2wPVJe&ust=1747213426250000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJDC-a6LoI0DFQAAAAAdAAAAABAE')
    if st.button('prova a cliccare'):
        st.text("hai superato la prova!!")
        st.balloons()

if __name__ == "__main__":
    main()