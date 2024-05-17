from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastApi.database import crud, models, schema
from fastApi.database.connect import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/trudovaya_knizhka/", response_model=schema.TrudovayaKnizhka)
def create_trudovaya_knizhka(trudovaya_knizhka: schema.TrudovayaKnizhkaCreate, db: Session = Depends(get_db)):
    return crud.create_trudovaya_knizhka(db=db, trudovaya_knizhka=trudovaya_knizhka)


@app.get("/trudovaya_knizhka/", response_model=list[schema.TrudovayaKnizhka])
def read_trudovaya_knizhki(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    trudovaya_knizhki = crud.get_trudovaya_knizhki(db, skip=skip, limit=limit)
    return trudovaya_knizhki


@app.get("/trudovaya_knizhka/{trudovaya_knizhka_id}", response_model=schema.TrudovayaKnizhka)
def read_trudovaya_knizhka(trudovaya_knizhka_id: int, db: Session = Depends(get_db)):
    db_trudovaya_knizhka = crud.get_trudovaya_knizhka(db, trudovaya_knizhka_id=trudovaya_knizhka_id)
    if db_trudovaya_knizhka is None:
        raise HTTPException(status_code=404, detail="Trudovaya Knizhka not found")
    return db_trudovaya_knizhka


@app.post("/trudovaya_knizhka/{trudovaya_knizhka_id}/work_info/", response_model=schema.WorkInfo)
def create_work_info(trudovaya_knizhka_id: int, work_info: schema.WorkInfoCreate, db: Session = Depends(get_db)):
    return crud.create_work_info(db=db, work_info=work_info, trudovaya_knizhka_id=trudovaya_knizhka_id)


@app.post("/trudovaya_knizhka/{trudovaya_knizhka_id}/award_info/", response_model=schema.AwardInfo)
def create_award_info(trudovaya_knizhka_id: int, award_info: schema.AwardInfoCreate, db: Session = Depends(get_db)):
    return crud.create_award_info(db=db, award_info=award_info, trudovaya_knizhka_id=trudovaya_knizhka_id)
