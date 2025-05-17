import streamlit as st

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def meters_to_yards(meters):
    return meters * 1.09361

def yards_to_meters(yards):
    return yards / 1.09361

def seconds_to_minutes(seconds):
    return seconds / 60

def minutes_to_seconds(minutes):
    return minutes * 60

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

st.title("🔢 Advanced Unit Converter")

conversion_type = st.selectbox("Choose a category:", [
    "Length", "Weight", "Temperature", "Time", "Volume"
])

if conversion_type == "Length":
    option = st.selectbox("Choose conversion:", [
        "Kilometers to Miles", "Miles to Kilometers", "Meters to Yards", "Yards to Meters"
    ])
    value = st.number_input("Enter value:")
    if st.button("Convert"):
        if option == "Kilometers to Miles":
            st.write(f"{value} km is equal to {km_to_miles(value):.2f} miles")
        elif option == "Miles to Kilometers":
            st.write(f"{value} miles is equal to {miles_to_km(value):.2f} km")
        elif option == "Meters to Yards":
            st.write(f"{value} meters is equal to {meters_to_yards(value):.2f} yards")
        elif option == "Yards to Meters":
            st.write(f"{value} yards is equal to {yards_to_meters(value):.2f} meters")

elif conversion_type == "Weight":
    option = st.selectbox("Choose conversion:", [
        "Kilograms to Pounds", "Pounds to Kilograms"
    ])
    value = st.number_input("Enter value:")
    if st.button("Convert"):
        if option == "Kilograms to Pounds":
            st.write(f"{value} kg is equal to {kg_to_pounds(value):.2f} pounds")
        elif option == "Pounds to Kilograms":
            st.write(f"{value} pounds is equal to {pounds_to_kg(value):.2f} kg")

elif conversion_type == "Temperature":
    option = st.selectbox("Choose conversion:", [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius"
    ])
    value = st.number_input("Enter value:")
    if st.button("Convert"):
        if option == "Celsius to Fahrenheit":
            st.write(f"{value}°C is equal to {celsius_to_fahrenheit(value):.2f}°F")
        elif option == "Fahrenheit to Celsius":
            st.write(f"{value}°F is equal to {fahrenheit_to_celsius(value):.2f}°C")

elif conversion_type == "Time":
    option = st.selectbox("Choose conversion:", [
        "Seconds to Minutes", "Minutes to Seconds"
    ])
    value = st.number_input("Enter value:")
    if st.button("Convert"):
        if option == "Seconds to Minutes":
            st.write(f"{value} seconds is equal to {seconds_to_minutes(value):.2f} minutes")
        elif option == "Minutes to Seconds":
            st.write(f"{value} minutes is equal to {minutes_to_seconds(value):.2f} seconds")

elif conversion_type == "Volume":
    option = st.selectbox("Choose conversion:", [
        "Liters to Gallons", "Gallons to Liters"
    ])
    value = st.number_input("Enter value:")
    if st.button("Convert"):
        if option == "Liters to Gallons":
            st.write(f"{value} liters is equal to {liters_to_gallons(value):.2f} gallons")
        elif option == "Gallons to Liters":
            st.write(f"{value} gallons is equal to {gallons_to_liters(value):.2f} liters")
