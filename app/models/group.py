from enum import Enum
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions.alchemy import alchemy

class EducationLevel(Enum):
    bachelor = "Bachillerato"
    university = "Universitario"
    technical = "Técnico"

class Modality(Enum):
    online = "Online"
    presential = "Presencial"
    hybrid = "Hibrido"

class Group(UserMixin, alchemy.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    education_level: Mapped[EducationLevel] = mapped_column(Enum(EducationLevel))
    modality: Mapped[Modality] = mapped_column(Enum(Modality))