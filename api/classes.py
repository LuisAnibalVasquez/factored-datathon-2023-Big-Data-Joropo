from pydantic import BaseModel

class review(BaseModel):
    text:str

class sentiment(BasModel):
    label:str   
    score:numeric

    