import pandas as pd
import time
import streamlit as st
import plotly.express as px

# Create the title for the web app
st.title("My First Streamlit App")


@st.cache
def load_dataset():
    dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
    return dataset


titanic_data = load_dataset()

st.header("Dataset Overview")
showing_data = st.checkbox("Show All Data", True)
if showing_data:
    st.dataframe(titanic_data)
else:
    st.write("The dataset is hidden. Check the box to show the data.")

st.header("Data Description")

selected_class = st.radio("Select Class", titanic_data['class'].unique())
subset_class = titanic_data[titanic_data['class'] == selected_class]
st.write(f"Number of Records With Class {selected_class}: {subset_class.shape[0]}")

selected_decks = st.multiselect("Select Decks", titanic_data['deck'].unique())
subset_decks = titanic_data[titanic_data['deck'].isin(selected_decks)]
st.write(f"Number of Records With Decks {selected_decks}: {subset_decks.shape[0]}")

selected_sex = st.selectbox("Select Sex", titanic_data['sex'].unique())
subset_sex = titanic_data[titanic_data['sex'] == selected_sex]
st.write(f"Number of Records With Sex {selected_sex}: {subset_sex.shape[0]}")

age_columns = st.beta_columns(2)
age_min = age_columns[0].number_input("Minimum Age", value=titanic_data['age'].min())
age_max = age_columns[1].number_input("Maximum Age", value=titanic_data['age'].max())
if age_max < age_min:
    st.error("The maximum age can't be smaller than the minimum age!")
else:
    st.success("Congratulations! Correct Parameters!")
    subset_age = titanic_data[(titanic_data['age'] <= age_max) & (age_min <= titanic_data['age'])]
    st.write(f"Number of Records With Age Between {age_min} and {age_max}: {subset_age.shape[0]}")


optionals = st.beta_expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

st.markdown("This is a _markdown_ comment, which is *great* and _**awesome**_.")
st.markdown("Here's the link to [Streamlit](https://www.streamlit.io/)")

st.write("Survival By Class")
st.dataframe(pd.crosstab(titanic_data['class'], titanic_data['survived'], normalize='index'))
st.write("Here's the code to generate this table:")
st.code("pd.crosstab(titanic_data['class'], titanic_data['survived'], normalize='index')")

with st.echo("below"):
    balloons = st.text_input("Please enter awesome to see some balloons")
    if balloons == "awesome":
        st.balloons()


st.write("This is a large text area.")
st.text_area("A very big area", height=300)

progress_bar = st.progress(0)
progress_text = st.empty()
for i in range(101):
    time.sleep(0.1)
    progress_bar.progress(i)
    progress_text.text(f"Progress: {i}%")

st.write(px.histogram(titanic_data['fare']))
