from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import create_engine
sqlite_database = "sqlite:///person.db"
engine = create_engine(sqlite_database)
class Base(DeclarativeBase): pass
class Film(Base):
    __tablename__ = "film"
    id = Column(Integer, primary_key=True, index=True)
    name_film = Column(String)
    year_relaise = Column(Integer)
    genre_film = Column(String)
    ranked = Column(String)

Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    def add_book():
        book = Film(name_film="Metro 2023", year_relaise=2023, genre_film="horor", ranked="9.5")
        db.add(book)
        db.commit()
    add_book()

    def read_book():
        book_read = db.query(Film).all()
        book_read_filter = db.query(Film).filter(Film.year_relaise == 2023).all()
    read_book()

    def reload_book():
        book_read_reload = db.query(Film).filter(Film.id==1).first()
        if (book_read_reload != None):
            print(f"{book_read_reload.name_film} ({book_read_reload.year_relaise})")

            book_read_reload.name_film = "Book_3"
            book_read_reload.year_relaise = 2019

            db.commit()
    reload_book()

    def delete_book():
        book_delete = db.query(Film).filter(Film.name_film=='Book_3').first()
        db.delete(book_delete)
        db.commit()
    delete_book()