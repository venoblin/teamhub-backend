import bcrypt
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET')

def create_token(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")