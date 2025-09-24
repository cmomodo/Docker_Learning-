from flask import Flask
import pymysql



app = Flask(__name__)

@app.route('/')
def hello_world():

    #connect to the sql database
    db = pymysql.connect(
        host="mydb",
        user="root",
        passwd="my-secret-pw",
        db="mysql"
    )

    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, world mysql version : {version[0]}'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)