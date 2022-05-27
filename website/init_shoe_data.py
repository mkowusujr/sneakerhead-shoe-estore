import pandas as pd
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import random
import numpy as np
from .models import Shoe, Color, Quantity_Per_Size


# setup db
engine = db.create_engine('sqlite:///website/sneakerhead.db')
Session = sessionmaker(bind=engine)
session = Session()
COLORS_LIST_FILE = 'website/generating_data_resources/colors-list.txt'

def read_txt_file_as_list(filename):
	txt_file = open(filename, "r")
	file_content = txt_file.read()
	content_list = file_content.split("\n")
	return content_list


def set_up_quantities(shoe):
	colors_list = read_txt_file_as_list(COLORS_LIST_FILE)

	amount_of_colors = [1,2,3,4,5,6,7,8]
	probability = [.30, .20, .15, .05, .075, .075, .075, .075]
	how_many_colors = np.random.choice(
		amount_of_colors,1,p=probability )[0]

	selected_colors = []
	for i in range(1, how_many_colors + 1):
		rand_color = random.choice(colors_list)
		selected_colors.append(rand_color)

	for color in selected_colors:
		shoe_color = Color(color=color)
		session.add(shoe_color)
		for size in np.arange(6, 15.5, .5):
			quan_n_size = Quantity_Per_Size(size=size, quantity=10)
			session.add(quan_n_size)
			shoe_color.quan_per_size.append(quan_n_size)
			session.add(shoe_color)
		shoe.colors.append(shoe_color)
		session.add(shoe)
	session.commit()


def add_male_shoes():
    df = pd.read_csv('website/generating_data_resources/shoe_dataset.csv') # male data
    for index, row in df.iterrows():
        price = row['Prices']
        if len(price) > 1:
            price_list = price.split(" ")
            price = price_list[0]
        shoe = Shoe(
            name=row['Styles'],
            brand=row['Brands'],
            audience='Men',
            price=price
        )
        session.add(shoe)
        set_up_quantities(shoe)
    session.commit()


def populate_db_with_shoes():
	add_male_shoes()
