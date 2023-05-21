# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import relationship, Session
# from __future__ import annotations
# from typing import List
#
# from sqlalchemy import ForeignKey
# from sqlalchemy import Integer
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy import MetaData, Table, Column, Integer, ARRAY
#
#
#
# sqlite_database = "sqlite:///metanit2.db"
# engine = create_engine(sqlite_database)
#
# class Base(DeclarativeBase): pass
#
#
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     position = Column(String)
#     experiance = Column(Integer)
#     users = relationship("Company", back_populates="com")
#
#
# class Company(Base):
#     __tablename__ = "position"
#     id = Column(Integer, primary_key=True, index=True)
#     name_position = Column(String)
#     users = relationship("User", back_populates="company")
#
#
# Base.metadata.create_all(bind=engine)
#
# with Session(autoflush=False, bind=engine) as db:
#     # создаем компании
#     microsoft = Company(name="Microsoft")
#     google = Company(name="Google")
#     # создаем пользователей
#     tom = User(name="Tom")
#     bob = User(name="Bob")
#     # устанавливаем для компаний списки пользователей
#     microsoft.users = [tom]
#     google.users = [bob]
#     # добавляем компании в базу данных, и вместе с ними добавляются пользователи
#     db.add_all([microsoft, google])
#     db.commit()
#
#     # можно отдельно добавить объект в список
#     alice = User(name="Alice")
#     google.users.extend([alice])  # добавляем список из одного элемента
#
#     # можно установить для пользователя определенную компанию
#     sam = User(name="Sam")
#     sam.company = microsoft
#     db.add(sam)
#     db.commit()


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Session, relationship

sql_database = "sqlite:///User_prof.db"
engine = create_engine(sql_database)


class Base(DeclarativeBase):
    pass

asocciation_table = Table('asocciation_table', Base.metadata,
                          Column('user_post_id', Integer, ForeignKey('user_post.id')),
                          Column('user_id', Integer, ForeignKey('user.id')))

class User_post(Base):
    __tablename__ = "user_post"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    list_user = relationship("User",secondary=asocciation_table, back_populates="user_post")



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    experience = Column(Integer)
    user_post_id = Column(Integer, ForeignKey("user_post.id"))
    user_post = relationship("User_post", secondary=asocciation_table, back_populates="list_user")



Base.metadata.create_all(bind=engine)
db = Session(autoflush=False, bind=engine)


with Session(autoflush=False, bind=engine) as db:
    user_post_1 = User_post(name="DevOps")
    user_post_2 = User_post(name="Тестирование")
    user_post_3 = User_post(name="Програмист")

    db.add_all([user_post_1, user_post_2, user_post_3])
    db.commit()

    people_1 = User(name="Isma", experience = 20)
    people_2 = User(name="Egor", experience = 21)
    people_3 = User(name="Denis", experience = 22)
    people_1.user_post.append(user_post_1)
    db.add_all([people_1, people_2, people_3])
    db.commit()


    user_input = input()
    users_db = db.query(User).filter(User.name == user_input).all()
    for i in users_db:
        for j in i.user_post:
            print(j.name)

    user_input = input()
    users_db = db.query(User).filter(User.experience >= 5).all()
    for i in users_db:
        for j in i.user_post:
            if j.name == user_input:
                print(i.name)


#experience=3 experience=99 experience=6