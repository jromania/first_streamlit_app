import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title("My Parents New Healhty Diner")
streamlit.header("Breakfast Menu")
streamlit.text('🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinich & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi',key='1111')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")


# # write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


# fruit_choice2 = streamlit.text_input('What fruit would you like information about?','Kiwi',key='22222')
# streamlit.write('The user entered ', fruit_choice2)
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute(f"SELECT * from fruit_load_list where FRUIT_NAME = '{fruit_choice2}'")
# my_data_row = my_cur.fetchall()
# streamlit.dataframe(my_data_row)
 

 

# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response)


