from flask import Flask
from app.database import create_database

app = Flask(__name__)
create_database()

from app import routes
