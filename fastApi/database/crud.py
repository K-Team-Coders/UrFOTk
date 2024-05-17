from sqlalchemy.orm import Session
from fastApi.database import models, schema


def create_trudovaya_knizhka(db: Session, trudovaya_knizhka: schema.TrudovayaKnizhkaCreate):
    db_trudovaya_knizhka = models.TrudovayaKnizhka(**trudovaya_knizhka.dict())
    db.add(db_trudovaya_knizhka)
    db.commit()
    db.refresh(db_trudovaya_knizhka)
    return db_trudovaya_knizhka


def get_trudovaya_knizhki(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TrudovayaKnizhka).offset(skip).limit(limit).all()


def get_trudovaya_knizhka(db: Session, trudovaya_knizhka_id: int):
    return db.query(models.TrudovayaKnizhka).filter(models.TrudovayaKnizhka.id == trudovaya_knizhka_id).first()


def create_work_info(db: Session, work_info: schema.WorkInfoCreate, trudovaya_knizhka_id: int):
    db_work_info = models.WorkInfo(**work_info.dict(), trudovaya_knizhka_id=trudovaya_knizhka_id)
    db.add(db_work_info)
    db.commit()
    db.refresh(db_work_info)
    return db_work_info


def create_award_info(db: Session, award_info: schema.AwardInfoCreate, trudovaya_knizhka_id: int):
    db_award_info = models.AwardInfo(**award_info.dict(), trudovaya_knizhka_id=trudovaya_knizhka_id)
    db.add(db_award_info)
    db.commit()
    db.refresh(db_award_info)
    return db_award_info
