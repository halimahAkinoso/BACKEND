from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import bcrypt
import uvicorn

load_dotenv()

app = FastApI(title="Simple App", version="1.0.0")
class Simple(BaseModel):
    name: str = Field(..., example="Sam LARRY")
    email:str = Field(..., example="sam@gmail.com")
    password: str = Field(...,example="sam123")
    
    @app.post("/signup")
    def signup(input: simple):
        try:
            duplicate_query = text("""
                SELECT * FROM users
                WHERE email = :email
                         """)
            query = text("""
                INSERT INTO users(name, email, password)
                VALUES (:name, :email, :password)
                         """)
            salt = bcrypt.gensalt()
            hashedPassword = bcrypt.hashpw(input.password.encode('utf-8', salt))
            print(hashedPassword)
            
            db.execute(query, {"name": input.name, "email": input.email, "password": input.password})
            db.commit()
            
            return{"message": "user created successfully",
                   "data": {"name": input.name, "email": input.email}}
        except Exception as e:
            raise HTTPException(status_code=500, detail = e)
