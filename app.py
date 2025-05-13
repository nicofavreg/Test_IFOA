import streamlit as st

def main():
    st.title("questa è la creazione di un'applicazione")
    st.divider()
    st.header("capitolo 1")
    if st.button('prova a cliccare'):
        st.success('brava! hai superato il test')
        st.balloons()
        st.image('lempuyang.jpg')
    st.header("capitolo 2")    
    if st.toggle('test toggle'):
        st.write('test 2 superato')
    
    st.checkbox('spunta')

if __name__ == "__main__":
    main()