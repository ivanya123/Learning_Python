from sqlalchemy import create_engine, text, Table, Column, Integer, String, ForeignKey, insert
import psycopg2
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional
from sqlalchemy import MetaData

engine = create_engine('postgresql+psycopg2://postgres:112233@localhost:5432/Picture_bot', echo=True)
metadata = MetaData()
import json


# with engine.connect() as conn:
#     conn.execute(text('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))'))
#     conn.execute(
#         text("INSERT INTO users (username, password) VALUES (:username, :password)"),
#         [{"username": "admin", "password": "admin"},
#          {"username": "user2", "password": "user2"}]
#     )
#     conn.commit()

# with engine.begin() as conn:
#     conn.execute(text("INSERT INTO users (username, password) VALUES (:username, :password)"),
#                  [{"username": "qwer", "password": "qwerty"},
#                   {"username": "user2", "password": "user2"}]
#                  )


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM users"))
#     for row in result:
#         print()
#         print(f"username: {row.username}, password: {row.password}")
#         break

# stmt = text("SELECT username, password FROM users WHERE username = :username ORDER BY username")
# with Session(engine) as session:
#     result = session.execute(stmt, {"username": "admin"})
#     for row in result:
#         print(f"username: {row.username}, password: {row.password}")


# with Session(engine) as session:
#     result = session.execute(
#         text("UPDATE users SET password = :password WHERE username = :username"),
#         [
#             {"username": "admin", "password": "qwerty"},
#             {"username": "user2", "password": "112233"}
#         ]
#     )
#     session.commit()


# table_2 = Table(
#     "pictures",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("canvas_shape", String(30), nullable=False),
#     Column("canvas_base", String(30), nullable=False),
#     Column("canvas_size", String(30), nullable=False),
#     Column("canvas_height_and_width", String(30), nullable=False),
#     Column("price", Integer, nullable=False)
# )
#
# table = Table(
#     "buyers",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("username", String(30), nullable=False),
#     Column("chat_id", String(20)),
#     Column("picture_id", ForeignKey("pictures.id"), nullable=False)
# )
#
# metadata.drop_all(engine)

class Base(DeclarativeBase):
    pass


class Picture(Base):
    __tablename__ = "pictures"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    canvas_shape: Mapped[str] = mapped_column(String(30))
    canvas_base: Mapped[str] = mapped_column(String(30), nullable=False)
    canvas_size: Mapped[str] = mapped_column(String(30), nullable=False)
    canvas_height_and_width: Mapped[str] = mapped_column(String(30), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)

    buyers: Mapped[List["Buyer"]] = relationship(back_populates="picture")


class Buyer(Base):
    __tablename__ = "buyers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    chat_id: Mapped[str] = mapped_column(String(20))
    picture_id = mapped_column(ForeignKey("pictures.id"), nullable=False)

    picture: Mapped[Picture] = relationship(back_populates="buyer")


# Base.metadata.create_all(engine)

users = Table("users", metadata, autoload_with=engine)

# stmt = insert(users).values(username="king", password="admin")
# compiled = stmt.compile()
# print(compiled.params)
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()


def add_picture(canvas_shape: str, canvas_base: str, canvas_size: str, canvas_height_and_width: str, price: int):
    stmt = insert(Picture).values(canvas_shape=canvas_shape, canvas_base=canvas_base, canvas_size=canvas_size,
                                  canvas_height_and_width=canvas_height_and_width, price=price)
    with Session(engine) as session:
        session.execute(stmt)
        session.commit()


with open("info.json", 'r') as f:
    data = json.load(f)


for shape in data:
    for base in data[shape]:
        for size in data[shape][base]:
            for height_and_width in data[shape][base][size]:
                price = data[shape][base][size][height_and_width]
                add_picture(shape, base, size, height_and_width, price)
