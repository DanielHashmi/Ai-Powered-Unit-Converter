import google.generativeai as genai

from dotenv import load_dotenv
import os
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def convert_units(value, from_unit, to_unit):
    prompt = f"Convert {value} {from_unit} to {to_unit} and output just the result in this ''"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return str(e)


unit_categories = {
    "Area": [
        "square_kilometer", "square_meter", "square_mile", "square_yard",
        "square_foot", "square_inch", "hectare"
    ],
    "Data Transfer Rate": [
        "bit_per_second", "kilobit_per_second", "kilobyte_per_second", "kibibit_per_second",
        "megabit_per_second", "megabyte_per_second", "mebibit_per_second",
        "gigabit_per_second", "gigabyte_per_second", "gibibit_per_second",
        "terabit_per_second", "terabyte_per_second", "tebibit_per_second"
    ],
    "Digital Storage": [
        "kilobit", "megabit", "mebibit", "gigabit", "terabit", "tebibit", "petabit", "pebibit",
        "kilobyte", "megabyte", "mebibyte", "gigabyte", "terabyte", "tebibyte"
    ],
    "Energy": [
        "joule", "kilojoule", "gram_calorie", "kilocalorie", "watt_hour",
        "kilowatt_hour", "electronvolt", "british_thermal_unit", "us_therm", "foot_pound"
    ],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": [
        "mile_per_us_gallon", "mile_per_gallon", "kilometer_per_liter", "liter_per_100_kilometers"
    ],
    "Length": [
        "centimeter", "kilometer", "millimeter", "micrometer", "nanometer", "mile", "yard",
        "foot", "inch", "nautical_mile"
    ],
    "Mass": [
        "tonne", "kilogram", "gram", "milligram", "imperial_ton", "us_ton", "pound"
    ],
    "Plane Angle": [
        "degree", "gradian", "milliradian", "minute_of_arc", "radian"
    ],
    "Pressure": [
        "bar", "pascal", "pound_per_square_inch", "standard_atmosphere", "torr"
    ],
    "Speed": [
        "mile_per_hour", "foot_per_second", "meter_per_second", "kilometer_per_hour"
    ],
    "Temperature": ["degree_Celsius", "fahrenheit", "kelvin"],
    "Time": [
        "nanosecond", "microsecond", "millisecond", "second", "minute", "hour", "day",
        "week", "month", "calendar_year", "decade", "century"
    ],
    "Volume": [
        "us_liquid_gallon", "us_liquid_quart", "us_liquid_pint", "us_legal_cup", "us_fluid_ounce",
        "us_tablespoon", "us_teaspoon", "cubic_meter", "liter", "milliliter", "imperial_gallon",
        "imperial_quart", "imperial_pint", "imperial_cup", "imperial_fluid_ounce",
        "imperial_tablespoon", "imperial_teaspoon", "cubic_foot", "cubic_inch"
    ]
}
