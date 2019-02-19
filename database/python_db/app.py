from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True)
    title = Column('title', String(32))

    def __init__(self, title):
        self.title = title


print('Here 1')
engine = create_engine('mysql+mysqlconnector://app:app@db/app')

# Continue attempting to connect until successful
while True:
    try:
        engine.connect()
        break
    except:
        pass

Base.metadata.create_all(engine)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

p1 = Product('ketchup')
session.add(p1)

session.commit()
session.close()

print("Done.")
