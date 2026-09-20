import requests
import streamlit as st

st.set_page_config(
    page_title="My Weather App",
    page_icon="⛅",
)

st.title("🌤️ Simple Weather App MADE BY BC MARUF")
st.write("a bukachuda city dis naile kick khabi")

api = "d2634743380898849931b9a0fc9c3c1b"
user_input = st.text_input("Enter your city:")

if st.button("Get Weather"):
    
    if user_input:
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api}"
        weather_data = requests.get(url)
        
        
        if weather_data.status_code == 200:
            data = weather_data.json()
            weather = data['weather'][0]['main']
            temperature = data['main']['temp']
            
            
            st.success(f"Weather in {user_input.title()}: **{weather}**")
            st.metric(label="Temperature", value=f"{temperature} °F")
        else:
            st.error("City not found! Please check the spelling and try again.")
    else:
            st.warning("Please enter a city name first.")
