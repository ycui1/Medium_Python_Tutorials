import streamlit as st
import pandas as pd

st.title("My First Web App")

st.header("Titanic Dataset")
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
st.write(df)

st.header("Fare Cumulative")
fare = df['fare'].cumsum()
st.line_chart(fare)

st.header("Code Snippet")
st.code("""a = 100
b = 'text'
c = [1, 2, 3]""")

st.header("Interactive Widgets")
st.radio("Choose One", ["To be", "Not to be"])
st.slider("How old are you?", min_value=1, max_value=100)
st.date_input("Choose your favorite date")

st.header("Show Balloons")
your_energy = st.slider(
    "Try setting your energy level to 90 or above",
    min_value=1,
    max_value=100
)
if your_energy >= 90:
    st.balloons()