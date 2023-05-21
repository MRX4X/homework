from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import create_engine
sqlite_database = "sqlite:///person.db"
engine = create_engine(sqlite_database)
class Base(DeclarativeBase): pass
class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    # username = Column(String, nullable=False)
    # password = Column(String, UniqueConstraint, nullable=False)
    username = Column(String)
    password = Column(String)

Base.metadata.create_all(bind=engine)

print("Привет. Выбери зарегистрироваться - введи 1 или авторизироваться - введи 2")
choise_user = int(input())
if choise_user == 1:
    print("Введи логин")
    login_user = input()
    print("Введи пароль")
    pass_user = input()
    with Session(autoflush=False, bind=engine) as db:
        inser_user = User(username=login_user, password = pass_user)
        db.add(inser_user)
        db.commit()

    print("Вы успешно зарегистрировались")

if choise_user == 2:
    print("Введи логин")
    login_user = input()
    print("Введи пароль")
    pass_user = input()
    with Session(autoflush=False, bind=engine) as db:
        select_user = db.query(User).filter(User.username == login_user and User.password == pass_user).all()
    if login_user == select_user[0] and pass_user == select_user[1]:
        print("Вы успешно авторизировались")
    else:
        print("Вы не правильно ввели логин или пароль")