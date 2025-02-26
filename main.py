from converter import convert_units, unit_categories
import streamlit as st

st.title("🔥AI Powered Unit Converter")

# Select category
category = st.selectbox("Select a category", list(unit_categories.keys()))

# Select units
from_unit = st.selectbox("Convert from", unit_categories[category])
to_unit = st.selectbox("Convert to", unit_categories[category])

# Input value to convert
value = st.number_input("Enter value to convert", min_value=0.0, format="%f")

# Perform conversion
if st.button("Convert"):
    with st.spinner('Converting...'):
        result = convert_units(value, from_unit, to_unit)
    st.success(f"{result}")
