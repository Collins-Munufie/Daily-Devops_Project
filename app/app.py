from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
    try:
        db = MySQLdb.connect(
            host="localhost",
            user="devuser",
            passwd="Khopi!@2018",
            db="devsecops_db"
        )
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        return f"MySQL version: {version[0]}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
