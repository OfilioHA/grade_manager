from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Enum as SAEnum
from app.extensions.alchemy import alchemy

class Course(alchemy.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[bool] = mapped_column(default=True, nullable=False)
    support_file: Mapped[str] = mapped_column(String(255), nullable=True)
    #Relations
    topics = relationship("CourseTopic", back_populates="course", cascade="all, delete-orphan")
    files = relationship("CourseBibliography", back_populates="course", cascade="all, delete-orphan")

class CourseTopic(alchemy.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content_path: Mapped[str] = mapped_column(String(255))
    # Relations
    course = relationship("Course", back_populates="topics")

class SourceType(Enum):
    url = "Sitio Web"    
    file = "Archivo"

class CourseBibliography(alchemy.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    source_type: Mapped[SourceType] = mapped_column(SAEnum(SourceType, name="source_type_enum", native_enum=False))
    source_value: Mapped[str] = mapped_column(String(255))
    # Relations
    course = relationship("Course", back_populates="files")