##an  alternative way of building connection
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

connection = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

print("Connected to MySQL successfully!")

cursor = connection.cursor(pymysql.cursors.DictCursor)

