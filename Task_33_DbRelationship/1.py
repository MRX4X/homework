from sqlalchemy import *
from sqlalchemy.orm import *
sqlite_database = "sqlite:///person1.db"
engine = create_engine(sqlite_database)

class Base(DeclarativeBase): pass
class User_book(Base):
    __tablename__ = "User_book"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    book = relationship("Book", back_populates="users")


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author = Column(String)
    id_user = Column(Integer, ForeignKey("User_book.id"))
    users = relationship("User_book", back_populates="book")

Base.metadata.create_all(bind=engine)

# with Session(autoflush=False, bind=engine) as db:
#     # создаем компании
#     metro2023 = Book(name="Metro2023",author = "oleg")
#     skaski = Book(name="Skaski",author = "pushkin")
#
#     # создаем пользователей
#     tom = User_book(name="Tom")
#     bob = User_book(name="Bob")
#     # устанавливаем для компаний списки пользователей
#     tom.book.extend([metro2023])
#     # добавляем компании в базу данных, и вместе с ними добавляются пользователи
#     db.add(tom)
#     db.commit()
with Session(autoflush=False,bind = engine) as db:
    def User_search_book():
        input_user=input()
        users = db.query(User_book).filter(User_book.name==input_user).all()
        for user in users:
            for book in user.book:
                print(book.name)
    User_search_book()
    # можно отдельно добавить объект в список
    # alice = User(name="Alice")
    # google.users.extend([alice])  # добавляем список из одного элемента
    #
    # # можно установить для пользователя определенную компанию
    # sam = User(name="Sam")
    # sam.company = microsoft
    # db.add(sam)
    # db.commit()

