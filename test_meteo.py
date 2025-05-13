import requests
import os
import pandas as pd
import streamlit as st
# from dotenv import load_dotenv
import math
from datetime import datetime
# load_dotenv()

API_key = st.secrets["api_key"]
# API_key = os.getenv('api_key')



def main():
    st.title("Applicazione Meteo 🌞")
    st.text("creata da Nico")
    st.divider()

    
    city_name = st.text_input('inserisci la città:', "reggiolo")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result = requests.get(url)
    json = result.json()
   # st.json(json)
    temp_max = json['main']['temp_max'] - 273.15 # temperatura massima
    temp_max = round(temp_max, 2)
    temp_min = json['main']['temp_min'] - 273.15 # temperatura massima
    temp_min = round(temp_min, 2)
    latitudine = json['coord']['lat'] #latitudine
    longitudine = json['coord']['lon'] #longitudine
    df = pd.DataFrame([[latitudine, longitudine]], columns=['lat', 'lon'])
    temperatura = json['main']['temp'] - 273.15 #temperatura
    temperatura = round(temperatura, 2)
    temp_percepita = json['main']['feels_like'] - 273.15
    temp_percepita = round(temp_percepita, 2)
    pressione = json['main']['pressure'] #pressione atmosferica hPa
    umidita = json['main']['humidity'] #umidità in %
    visibilita = json['visibility'] #visitbilità
    vel_vento = json['wind']['speed'] #velocità vento m/s
    stato = json['sys']['country'] #stato
    alba =json['sys']['sunrise'] #alba
    alba = datetime.fromtimestamp(alba)
    alba = pd.Timestamp(alba).time()
    tramonto =json['sys']['sunset'] #tramonto
    tramonto = datetime.fromtimestamp(tramonto)
    tramonto = pd.Timestamp(tramonto).time()
    citta = json['name'] #città
    liv_mare = json['main']['sea_level'] #metri sopra il livello del mare
    descr = json['weather'][0]['description'] # descrizione
    situa = json['weather'][0]['main'] #situazione generale
    direzione = json['wind']['deg'] #direzione vento in gradi °
    raffiche = json['wind']['gust'] #raffiche vento m/s
    pressione_suolo = json['main']['grnd_level'] #pressione del suolo hPa

    col1,col2 = st.columns(2)
    with col1:
        st.write(citta, stato)
        st.write(f'temperatura attuale: {temperatura}°')
        st.write(f'percepita: {temp_percepita}°')
        st.write(f'massima: {temp_max}°')
        st.write(f'minima: {temp_min}°')
        st.write(f"l'alba è alle ore {alba}")
    with col2:
        st.write(situa)
        st.write(f'umidità: {umidita}%')
        st.write(f'visibilità: {visibilita} metri')
        st.write(f'velocità vento: {vel_vento} m/s con raffiche di {raffiche} m/s')
        st.write(f'pressione atmosferica: {pressione} hPa')
        st.write(f"il tramonto è alle ore {tramonto}")

    st.divider()    
    
    st.map(data= df, size=500)


if __name__ == "__main__":
    main()