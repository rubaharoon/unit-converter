import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Magic Unit Converter ✨", page_icon="🔮", layout="centered")

# Custom CSS for Enhanced UI
def custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #FFE4E1 !important;
            }
            .stApp {
                background-color: #FFE4E1;
                color: #333 !important;
                font-family: 'Comic Sans MS', cursive;
            }
            .stTextInput input, .stNumberInput input, .stSelectbox select {
                background-color: #FFF !important;
                color: #000 !important;
                border-radius: 8px;
                padding: 6px;
            }
            .stButton button {
                background-color: #FF69B4 !important;
                color: white !important;
                border-radius: 20px;
                font-size: 18px;
                transition: 0.3s;
                padding: 10px 20px;
            }
            .stButton button:hover {
                background-color: #ff4786 !important;
                transform: scale(1.05);
            }
            .success-box {
                background-color: #FFF;
                color: #FF1493;
                padding: 15px;
                border-radius: 12px;
                font-weight: bold;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
custom_css()

# Title and Description
st.markdown("""
    <h1 style='text-align: center;'>Magic Unit Converter ✨🔮</h1>
    <h3 style='text-align: center; color: #FF69B4;'>Effortless conversions with a touch of magic! 🪄💫</h3>
    <p style='text-align: center;'>
        No more tedious calculations—just select, input, and watch the magic happen! 🎩🔢 
        The easiest way to transform units instantly. 🌟✨ Try it now! 🚀🔮
    </p>
""", unsafe_allow_html=True)

# Conversion Categories
with st.container():
    st.subheader("Select Conversion Type 🛠️")
    conversion_type = st.selectbox("", [
        "Length", "Weight", "Temperature", "Area", "Volume", "Speed", "Time", "Energy", "Pressure"
    ])

# Conversion Functions
def convert_units(value, from_unit, to_unit, conversion_dict):
    return value * (conversion_dict[to_unit] / conversion_dict[from_unit])

def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("celsius", "fahrenheit"): lambda v: (v * 9/5) + 32,
        ("fahrenheit", "celsius"): lambda v: (v - 32) * 5/9,
        ("celsius", "kelvin"): lambda v: v + 273.15,
        ("kelvin", "celsius"): lambda v: v - 273.15,
        ("fahrenheit", "kelvin"): lambda v: (v - 32) * 5/9 + 273.15,
        ("kelvin", "fahrenheit"): lambda v: (v - 273.15) * 9/5 + 32,
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

# Unit Dictionaries
unit_dicts = {
    "Length": {"meters": 1, "kilometers": 0.001, "centimeters": 100, "inches": 39.37, "feet": 3.281, "miles": 0.000621},
    "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
    "Area": {"square_meters": 1, "square_kilometers": 0.000001, "square_feet": 10.7639, "acres": 0.000247105},
    "Volume": {"liters": 1, "milliliters": 1000, "gallons": 0.264172, "cubic_feet": 0.0353147},
    "Speed": {"m/s": 1, "km/h": 3.6, "mph": 2.237, "knots": 1.944},
    "Time": {"seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400},
    "Energy": {"joules": 1, "kilojoules": 0.001, "calories": 0.239, "kWh": 2.7778e-7},
    "Pressure": {"pascals": 1, "bar": 1e-5, "psi": 0.000145, "atm": 9.8692e-6}
}

# Input Fields
with st.container():
    st.subheader("Enter the value to convert 🔢")
    value = st.number_input("", value=1.0)
    
    units = unit_dicts.get(conversion_type, {})
    if conversion_type == "Temperature":
        from_unit = st.selectbox("From 🌡️", ["celsius", "fahrenheit", "kelvin"])
        to_unit = st.selectbox("To 🌡️", ["celsius", "fahrenheit", "kelvin"])
        result = convert_temperature(value, from_unit, to_unit)
    else:
        from_unit = st.selectbox("From 👉", list(units.keys()))
        to_unit = st.selectbox("To 👈", list(units.keys()))
        result = convert_units(value, from_unit, to_unit, units)

# Convert Button
if st.button("Convert ✨"):
    with st.spinner("Converting... 💪"):  
        time.sleep(1)
        st.markdown(f"""
            <div class='success-box'>
                Converted value: <b>{result:.4f} {to_unit}</b> 🚀
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <h4 style='text-align: center;'>
        Made with ❤️ by Ruba Haroon
    </h4>
""", unsafe_allow_html=True)