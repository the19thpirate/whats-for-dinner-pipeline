from utils import sqlWorker
from datetime import datetime
from warnings import filterwarnings
filterwarnings("ignore")
import streamlit as st

st.cache(allow_output_mutation = True)
def main():
    data = sqlWorker.getLastRecords()
    return data 

data = main()
idx = data['id'].iloc[0] + 1

formContainer = st.form("Input form")
with formContainer:
    st.text("Last Record Inserted : ")
    st.dataframe(data)

    st.text("Insert New Records: ")
    primaryMeal = st.text_input("What is the Primary Meal: ", key = "primarymeal")
    secondaryMeal = st.text_input("Enter secondary meal: ", key = "secondarymeal")
    tertiaryMeal = st.text_input("Enter tertiary meal: ", key = "tertmeal")
    mealType = st.selectbox("Which meal is it? ", ("breakfast", "lunch", "dinner"))
    isHomecooked = st.selectbox("Is the meal homecooked? ", ("Yes", "No"))
    date_time = st.date_input("Enter Date and Time: ", key = "time")

    submitButton = st.form_submit_button("Submit")
    if submitButton:
        st.write(f"""
                ID: {idx},
                Primary Meal : {primaryMeal},
                Secondary Meal : {secondaryMeal},
                Tertiary Meal : {tertiaryMeal},
                Meal Type : {mealType},
                Homecooked? : {isHomecooked},
                Date : {date_time}
            """)
        insertData = [idx, primaryMeal, secondaryMeal, tertiaryMeal,
        mealType, isHomecooked, date_time]
        successText = sqlWorker.insertNewRecord(insertData)
        st.write(successText)
        






