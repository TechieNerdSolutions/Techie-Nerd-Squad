from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

connection = MySQLdb.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)

engine = create_engine(connection)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())