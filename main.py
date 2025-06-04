from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_roter
from order_routes import order_roter