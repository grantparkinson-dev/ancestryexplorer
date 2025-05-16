# backend/database/models.py
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base # Import Base from connection.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # We can add more fields like first_name, last_name, subscription_status later

    individuals = relationship("Individual", back_populates="owner")
    # Add relationship to GedcomFile if you plan to store raw files or metadata
    # gedcom_files = relationship("GedcomFile", back_populates="uploader")


class Individual(Base):
    __tablename__ = "individuals"

    id = Column(Integer, primary_key=True, index=True)
    # GEDCOM specific fields - keep simple for now
    gedcom_id = Column(String, index=True, nullable=True) # e.g., @I1@
    name = Column(String, index=True, nullable=False)
    sex = Column(String, nullable=True) # M, F, U

    birth_date = Column(String, nullable=True) # Store as string for flexibility with GEDCOM dates
    birth_place = Column(String, nullable=True)
    death_date = Column(String, nullable=True)
    death_place = Column(String, nullable=True)

    # Link to the user who uploaded/owns this data
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="individuals")

    # Relationships to other individuals (parents, spouses, children) will be more complex
    # and often managed via association tables or specific Family records.
    # We'll build these out incrementally. For now, this is a basic individual record.

# You might add other models later like:
# class Family(Base): ...
# class Event(Base): ...
# class GedcomFile(Base): ...