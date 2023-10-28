from pydantic import BaseModel

class UserScheme(BaseModel):
    name: str
    email: str
    password: str
    is_admin: bool   