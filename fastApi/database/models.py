from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TrudovayaKnizhka(Base):
    __tablename__ = 'trudovaya_knizhka'

    id = Column(Integer, primary_key=True, autoincrement=True)
    series = Column(String(10), nullable=False)
    number = Column(String(20), nullable=False)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=True)
    birth_year = Column(Integer, nullable=False)
    date_of_filling = Column(Date, nullable=False)

    changed_last_name = Column(String(50), nullable=True)
    changed_first_name = Column(String(50), nullable=True)
    changed_middle_name = Column(String(50), nullable=True)
    document_basis = Column(String(100), nullable=True)
    document_series = Column(String(10), nullable=True)
    document_number = Column(String(20), nullable=True)
    document_issue_date = Column(Date, nullable=True)
    document_issued_by = Column(String(100), nullable=True)

    work_info = relationship("WorkInfo", back_populates="trudovaya_knizhka")
    award_info = relationship("AwardInfo", back_populates="trudovaya_knizhka")


class WorkInfo(Base):
    __tablename__ = 'work_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    trudovaya_knizhka_id = Column(Integer, ForeignKey('trudovaya_knizhka.id'), nullable=False)
    date_of_hire = Column(Date, nullable=False)
    date_of_dismissal = Column(Date, nullable=True)
    stamp_description = Column(String(200), nullable=False)
    position_description = Column(String(200), nullable=False)
    order_number_date = Column(String(100), nullable=False)

    trudovaya_knizhka = relationship("TrudovayaKnizhka", back_populates="work_info")


class AwardInfo(Base):
    __tablename__ = 'award_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    trudovaya_knizhka_id = Column(Integer, ForeignKey('trudovaya_knizhka.id'), nullable=False)
    date = Column(Date, nullable=False)
    stamp_description = Column(String(200), nullable=False)
    award_description = Column(String(500), nullable=False)
    order_number_date = Column(String(100), nullable=False)

    trudovaya_knizhka = relationship("TrudovayaKnizhka", back_populates="award_info")


