# sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean,Integer
from sqlalchemy import engine

Base =  declarative_base()

class product (Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True)
    link = Column(String)
    title = Column(String)
    price = Column(String)
    oprice = Column(String)
    discount = Column(String)
    delivery = Column(String)
    deal_type = Column(String, default="")
    def __str__(self):
        return self.title
 

if __name__ == "__main__":
    engine = engine.create_engine('sqlite:///scraper.sqlite',
                                  echo=True)
    Base.metadata.create_all(engine)




    