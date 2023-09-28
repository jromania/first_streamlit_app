import streamlit
import pandas
import requests
import snowflake.connector


def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
   
def get_fruit_load_list():
   #fruit_choice2 = streamlit.text_input('What fruit would you like information about?','Kiwi',key='22222')
# streamlit.write('The user entered ', fruit_choice2)
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_cur = my_cnx.cursor()
   my_cur.execute(f"SELECT * from fruit_load_list")
   return my_cur.fetchall()
# 
 def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
       my_cur.execute(f"insert into fruit_load_list values ('{new_fruit}')"
       return f"Thanks for adding {new_fruit}"

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

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi',key='1111')
   if not fruit_choice:
      streamlit.error("Please select a fruit")
 
   else:
      
      streamlit.dataframe(get_fruityvice_data(fruit_choice))

except URLError as e:
  streamlit.error()
streamlit.header('The fruit list contains')
if streamlit.button('Get Fruit Load List'):
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi',key='2222')
if streamlit.button('Add a Fruit to the List'):
   back_from_function = insert_row_snowflake(add_my_fruit)

# # write your own comment -what does the next line do? 



 

# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response)


