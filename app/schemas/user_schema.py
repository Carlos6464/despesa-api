# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr

# Schema para receber dados na criação de um usuário
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Schema para retornar dados de um usuário (sem a senha)
class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True # Permite que o Pydantic leia dados de objetos SQLAlchemy