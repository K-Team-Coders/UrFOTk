from datetime import date
from pydantic import BaseModel


class WorkInfoBase(BaseModel):
    date_of_hire: date
    date_of_dismissal: date | None
    stamp_description: str
    position_description: str
    order_number_date: str


class WorkInfoCreate(WorkInfoBase):
    pass


class WorkInfo(WorkInfoBase):
    id: int
    trudovaya_knizhka_id: int

    class Config:
        orm_mode = True


class AwardInfoBase(BaseModel):
    date: date
    stamp_description: str
    award_description: str
    order_number_date: str


class AwardInfoCreate(AwardInfoBase):
    pass


class AwardInfo(AwardInfoBase):
    id: int
    trudovaya_knizhka_id: int

    class Config:
        orm_mode = True


class TrudovayaKnizhkaBase(BaseModel):
    series: str
    number: str
    last_name: str
    first_name: str
    middle_name: str | None
    birth_year: int
    date_of_filling: date
    changed_last_name: str | None
    changed_first_name: str | None
    changed_middle_name: str | None
    document_basis: str | None
    document_series: str | None
    document_number: str | None
    document_issue_date: date | None
    document_issued_by: str | None


class TrudovayaKnizhkaCreate(TrudovayaKnizhkaBase):
    pass


class TrudovayaKnizhka(TrudovayaKnizhkaBase):
    id: int
    work_info: list[WorkInfo] = []
    award_info: list[AwardInfo] = []

    class Config:
        orm_mode = True
