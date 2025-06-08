from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        dbname=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host=os.environ.get("POSTGRES_HOST")
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    cur.close()
    conn.close()
    return f"PostgreSQL version: {version[0]}"
