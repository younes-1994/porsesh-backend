from pydantic import BaseModel
from typing import List

class FormItem(BaseModel):
    name: str
    label: str
    value: str

class Form(BaseModel):
    items: List[FormItem]

    class Config:
        from_attributes = True
