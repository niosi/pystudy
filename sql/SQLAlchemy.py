# SQL ORM框架
from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from json import dumps, loads

Base = declarative_base()  # 对象基类


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(20), unique=True)


engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test', echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
newuser = User(uname='xiaoqi')
newuser2 = User(uname='leiba')
session.add_all((newuser, newuser2))
v = session.query(User).all()
for user in v:
    duser = user.__dict__
    print(duser["id"], duser["uname"])
session.commit()
session.close()
