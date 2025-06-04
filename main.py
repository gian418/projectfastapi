#para rodar o nosso codigo executar uvicorn main:app --reload
#pip3 install fastapi uvicorn sqlalchemy 'passlib[bcrypt]' 'python-jose[cryptography]' python-dotenv python-multipart
from fastapi import FastAPI

app = FastAPI()