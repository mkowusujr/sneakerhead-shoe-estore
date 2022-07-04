"""
A utility python program that populates the shoe store database
with data from csv files that have been preselected.

Author: Mathew Owusu Jr
"""


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
MENS_DATASET = 'website/generating_data_resources/mens_shoe_dataset.csv'
WOMENS_DATASET = 'website/generating_data_resources/womens_shoe_dataset.csv'


def read_txt_file_as_list(filename):
    """
    Opens a csv file and reads all the contents and stores each row into a 
    list

    Parameters:
        filename (string): The name of the csv file being read

    Returns:
        list of strings: The contents of the csv file as a list of strings
    """
    txt_file = open(filename, "r")
    file_content = txt_file.read()
    content_list = file_content.split("\n")
    return content_list


def set_up_quantities(shoe, smallest_size, largest_size):
    """
    Takes a shoe object and random generates the possible colors it
    can come in it. Then it generates the quantities for each color and
    shoe size combination.

    Parameters:
    shoe (Shoe Object): The Shoe object being modified
    smallest_size (int): The smallest size this shoe comes in
    largest_size (int): The largest suze this shoe comes in
    """
    colors_list = read_txt_file_as_list(COLORS_LIST_FILE)

    amount_of_colors = [1, 2, 3, 4, 5, 6, 7, 8]
    probability = [.30, .20, .15, .05, .075, .075, .075, .075]
    how_many_colors = np.random.choice(
    amount_of_colors, 1, p=probability)[0]

    selected_colors = []
    for i in range(1, how_many_colors + 1):
        rand_color = random.choice(colors_list)
        selected_colors.append(rand_color)

    for color in selected_colors:
        shoe_color = Color(color=color)
        session.add(shoe_color)
        for size in np.arange(smallest_size, largest_size + 0.5, .5):
            quan_n_size = Quantity_Per_Size(size=size, quantity=10)
            session.add(quan_n_size)
            shoe_color.quan_per_size.append(quan_n_size)
            session.add(shoe_color)
        shoe.colors.append(shoe_color)
        session.add(shoe)
    session.commit()


def add_male_shoes():
    """
    Opens and reads the mens shoes dataset and iterates through the rows in the
    csv file. Next it creates a new Shoe object using the data found in the columns
    of the create row. Then it saves the newly constucted shoe into the database.
    """
    df = pd.read_csv(MENS_DATASET)
    for index, col in df.iterrows():
        price = col['Prices']
        if len(price) > 1:
            price_list = price.split(" ")
            price = price_list[0]
            shoe = Shoe(
                name=col['Styles'],
                brand=col['Brands'],
                audience='Men',
                price=price
            )
        session.add(shoe)
        set_up_quantities(shoe, 6, 15)
    session.commit()


def add_female_shoes():
    """
    Opens and reads the womens shoes dataset and iterates through the rows in the
    csv file. Next it creates a new Shoe object using the data found in the columns
    of the create row. Then it saves the newly constucted shoe into the database.
    """
    df = pd.read_csv(WOMENS_DATASET)
    for index, col in df.iterrows():
        shoe = Shoe(
            name=col['name'],
            brand=col['brand'],
            audience='Women',
            price=col['prices.amountMax']
        )
        session.add(shoe)
        set_up_quantities(shoe, 4, 12)
    session.commit()


def populate_db_with_shoes():
    """
    Populates the database with data from the male and female shoe csv files
    """
    add_male_shoes()
    add_female_shoes()
