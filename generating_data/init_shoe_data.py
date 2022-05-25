import pandas as pd
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from ..website.models import Shoe
# setup db
engine = db.create_engine('sqlite:///website/sneakerhead.db')
# connection = engine.connect()
Session = sessionmaker(bind=engine)
# Session.configure(bind=engine)
session = Session()
df = pd.read_csv('shoe_dataset.csv')
# with engine.connect() as conn:
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
session.commit()
        # result = conn.execute(stmt)
        # conn.commit()
