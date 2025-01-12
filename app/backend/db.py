from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bine=engine)


class Base(DeclarativeBase):
    pass
