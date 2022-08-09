import streamlit

streamlit.title("my parents are preparing healthy dinner")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal🥣')
streamlit.text('Kale, Spinach & Rocket Smoothie🥗')
streamlit.text('Hard-Boiled Free-Range Egg🐔')
streamlit.text("avacado with toast 🥑🍞")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index),['Avocado' , 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#dispay badge
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output is the screen as table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
from urllib.error import urlerror

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load list contains")
streamlit.dataframe(my_data_rows)

#dont run anything past here a while trpubleshoot
stramlit.stop()

