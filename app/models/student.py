from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date
from datetime import date
from app.extensions.alchemy import alchemy

class Student(alchemy.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    identification: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=True)
    address: Mapped[str] = mapped_column(String(255), nullable=True)

    def get_fullname(self) -> str:
        return f"{self.firstname} {self.lastname}".strip()
