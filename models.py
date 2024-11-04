from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, primary_key=True)
    rule_string = Column(String)
    ast = Column(JSON)


engine = create_engine("sqlite:///rules.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
