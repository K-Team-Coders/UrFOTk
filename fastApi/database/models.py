from sqlalchemy import Column, Integer, String, ForeignKey
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
    birth_year = Column(String(10), nullable=False)
    date_of_filling = Column(String(50), nullable=False)

    changed_last_name = Column(String(50), nullable=True)
    changed_first_name = Column(String(50), nullable=True)
    changed_middle_name = Column(String(50), nullable=True)
    document_basis = Column(String(100), nullable=True)
    document_series = Column(String(10), nullable=True)
    document_number = Column(String(20), nullable=True)
    document_issue_date = Column(String(10), nullable=True)
    document_issued_by = Column(String(100), nullable=True)

    work_info = relationship("WorkInfo", back_populates="trudovaya_knizhka")
    award_info = relationship("AwardInfo", back_populates="trudovaya_knizhka")


class WorkInfo(Base):
    __tablename__ = 'worker_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    trudovaya_knizhka_id = Column(Integer, ForeignKey('trudovaya_knizhka.id'), nullable=False)
    date_of_hire = Column(String(20), nullable=True)
    date_of_dismissal = Column(String(20), nullable=True)
    stamp_description = Column(String(200), nullable=True)
    position_description = Column(String(200), nullable=True)
    order_number_date = Column(String(100), nullable=True)

    trudovaya_knizhka = relationship("TrudovayaKnizhka", back_populates="work_info")


class AwardInfo(Base):
    __tablename__ = 'award_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    trudovaya_knizhka_id = Column(Integer, ForeignKey('trudovaya_knizhka.id'), nullable=False)
    date = Column(String(20), nullable=True)
    stamp_description = Column(String(200), nullable=True)
    award_description = Column(String(500), nullable=True)
    order_number_date = Column(String(100), nullable=True)

    trudovaya_knizhka = relationship("TrudovayaKnizhka", back_populates="award_info")


