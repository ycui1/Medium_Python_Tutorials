import streamlit as st
# import seaborn as sns
#
# # Use the side bar
# penguins = sns.load_dataset("penguins")
# species = list(penguins['species'].unique())
# islands = list(penguins['island'].unique())
# chosen_species = st.sidebar.multiselect("Choose Specie(s)", species, species)
# chosen_islands = st.sidebar.multiselect("Choose Island(s)", islands, islands)
# chosen_data = penguins[penguins['species'].isin(chosen_species) & penguins['island'].isin(chosen_islands)]
#
# g = sns.jointplot(
#     data=chosen_data,
#     x="bill_length_mm", y="bill_depth_mm", hue="species",
#     kind="kde",
# )
# st.pyplot(g)


# Display Code Blocks
# st.write("Display Python Code")r
# st.code("fruits = ['apple', 'banana']\nhttp_response = (404, 'Page Not Found')")
#
# st.write("Display JavaScript Code")
# st.code("let fruits = ['apple', 'banana'];\nfunction sayHello():\n    console.log('Say Hello');", language="javascript")

# Display Code With Echo
# with st.echo():
#     fruits = ['apple', 'banana']
#     http_response = (404, 'Page Not Found')
#     st.radio("Choose Fruit", fruits)
#     st.text_input("HTTP Responses", http_response)

# Use Side bar

# with st.echo():
#     optionals = st.beta_expander("Optional Parameters", False)
#     optionals.checkbox("Enable Debugging")
#     optionals.radio("Pick Your Favorite", ["Apples", "Bananas", "Oranges"])

# Use columns
# with st.echo():
#     name_cols = st.beta_columns(3)
#     first_name = name_cols[0].text_input("First Name")
#     last_name = name_cols[1].text_input("Last Name")
#     middle_name = name_cols[2].text_input("Middle Name")

# Use radio as navigation
# panel_names = ["Panel 1", "Panel 2", "Panel 3"]
# chosen_panel = panel_names.index(st.sidebar.radio("Choose Panel", panel_names))
#
# if chosen_panel == 0:
#     st.header("Panel 1: Display Widgets")
# elif chosen_panel == 1:
#     st.header("Panel 2: Display Widgets")
# else:
#     st.header("Panel 3: Display Widgets")

# Use markdowns for emphasis
# with st.echo(code_location="below"):
#     st.markdown("Bold: This is a __bold__ parameter.")
#     st.markdown("Italic: This is an _italic_ parameter.")
#     st.markdown("Bold and italic: This has __*both*__.")
#     st.markdown("weblink: [Google](https://www.google.com/)")
#
#     st.subheader("A Section")
#     st.write("Lots of widgets here for the section.")
#     st.markdown("____")
#     st.subheader("Another Section")
#     st.write("Lots of widgets here for the section.")
#     st.markdown("____")
#
# with st.echo(code_location="below"):
#     import pandas as pd
#     import base64
#     data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
#     st.dataframe(data)
#     coded_data = base64.b64encode(data.to_csv(index=False).encode()).decode()
#     st.markdown(
#         f'<a href="data:file/csv;base64,{coded_data}" download="data.csv">Download Data</a>',
#         unsafe_allow_html=True
#     )


with st.echo(code_location="below"):
    texts = ["Text 1", "Text 2", "Text 3"]
    st.subheader("Without Container")
    st.write(texts[0])
    st.write(texts[1])
    st.write(texts[2])

    st.subheader("With Container")
    container = st.beta_container()
    container.write(texts[0])
    st.write(texts[1])
    container.write(texts[2])







