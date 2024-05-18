from typing import List, Optional

from pydantic import BaseModel


class WorkInfoBase(BaseModel):
    date_of_hire: str
    date_of_dismissal: Optional[str]
    stamp_description: str
    position_description: str
    order_number_date: str


class WorkInfoCreate(WorkInfoBase):
    pass


class WorkInfoOut(WorkInfoBase):
    id: int
    trudovaya_knizhka_id: int

    class Config:
        from_attributes = True


class AwardInfoBase(BaseModel):
    date: str
    stamp_description: str
    award_description: str
    order_number_date: str


class AwardInfoCreate(AwardInfoBase):
    pass


class AwardInfoOut(AwardInfoBase):
    id: int
    trudovaya_knizhka_id: int

    class Config:
        from_attributes = True


class TrudovayaKnizhkaBase(BaseModel):
    series: str
    number: str
    last_name: str
    first_name: str
    middle_name: Optional[str]
    birth_year: str
    date_of_filling: str
    changed_last_name: Optional[str]
    changed_first_name: Optional[str]
    changed_middle_name: Optional[str]
    document_basis: Optional[str]
    document_series: Optional[str]
    document_number: Optional[str]
    document_issue_date: Optional[str]
    document_issued_by: Optional[str]


class TrudovayaKnizhkaCreate(TrudovayaKnizhkaBase):
    work_info: Optional[List[WorkInfoCreate]] = []
    award_info: Optional[List[AwardInfoCreate]] = []


class TrudovayaKnizhkaOut(TrudovayaKnizhkaBase):
    id: int
    work_info: Optional[List[WorkInfoOut]] = []
    award_info: Optional[List[AwardInfoOut]] = []

    class Config:
        from_attributes = True
