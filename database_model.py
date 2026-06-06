from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,DateTime

Base = declarative_base()



class Actor(Base):

    __tablename__ = "actor"

    actor_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    last_update = Column(DateTime)
