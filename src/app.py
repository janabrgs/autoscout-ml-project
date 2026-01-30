import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Auto Preisvorhersage", layout="centered")
st.title("🚗 Auto Preisvorhersage App")
st.write("Gib die Fahrzeugdaten ein, um den geschätzten Preis zu berechnen.")

# Modell laden
rf_model = joblib.load(r"C:\Users\edson\Documents\Projekte\autoscout-ml-project\model\rf_model.pkl")

# Eingaben
brand = st.selectbox("Marke", ["Volkswagen", "Opel", "Ford", "Skoda", "Renault"])
model = st.selectbox("Modell", ["Golf", "Zafira", "Megane", "Scenic", "Transit"])
fuel = st.selectbox("Kraftstoff", ["Gasoline", "Diesel"])
gear = st.selectbox("Getriebe", ["Manual", "Automatic"])
offerType = st.selectbox("Angebotstyp", ["Used", "New"])
mileage = st.number_input("Kilometerstand", min_value=0, value=50000)
hp = st.number_input("PS", min_value=1, value=100)
year = st.number_input("Baujahr", min_value=1990, max_value=2026, value=2015)

# Preisvorhersage
if st.button("Preis schätzen"):
    X_new = pd.DataFrame([{
        "brand": brand,
        "model": model,
        "fuel": fuel,
        "gear": gear,
        "offerType": offerType,
        "mileage": mileage,
        "hp": hp,
        "year": year
    }])
    try:
        price = rf_model.predict(X_new)
        st.success(f"💰 Geschätzter Preis: {price[0]:,.0f} €")
    except Exception as e:
        st.error(f"Fehler bei der Vorhersage: {e}")