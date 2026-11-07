# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).
from pathlib import Path
import csv

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Volleyball Fan Survey",
    page_icon="🏐"
)

# PAGE TITLE AND USER DIRECTIONS
st.title("🏐 Volleyball Fan Popularity Survey")
st.write("Vote for your favorite professional volleyball player!")
st.info("🏐 Don't have a favorite player yet? Head over to the Visuals page to compare player statistics and discover your favorite!")
st.write("Help us find out which volleyball player is the most popular among fans.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
players = [
    "Aleksandar Nikolov",
    "Nik Mujanovic",
    "Ferre Reggers",
    "Ran Takahashi",
    "Adis Lagumdzija",
    "Kyle Hanes",
    "Rok Mozic",
    "Matt Anderson",
    "Mathis Henno",
    "Luciano Vicentin",
    "Bartlomiej Boladz",
    "Yuki Ishikawa",
    "Mattia Bottolo",
    "Darlan Souza",
    "Stephen Boyer",
    "Yuji Nishida"
]
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    category_input = st.selectbox("Who is your favorite volleyball player?",players)
    value_input = st.radio("Why is this player your favorite?",["Playing ability","Playing style","Personality","Leadership","Other"])

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Vote")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.
        
        file_path = Path(__file__).resolve().parent.parent / "data.csv"

        with open(file_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([category_input, value_input])

        st.success("Thank you for voting!")
        st.write("Favorite player:", category_input)
        st.write("Reason:", value_input)


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Fan Votes")

# Check if the CSV file exists and is not empty before trying to read it.
file_path = Path(__file__).resolve().parent.parent / "data.csv"
if file_path.exists() and file_path.stat().st_size > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv(file_path)
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("No votes have been submitted yet.")






