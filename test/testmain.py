'''
Created on 2019年12月2日

@author: baoyi
'''

if __name__ == '__main__':
    pass

from flask import Flask
app = Flask(__name__)

from util import mysql_util
db = mysql_util.MySqlUtil()

@app.route("/")
def hello_world():
    #return "hello world"
    sql = "select * from t_stockreport_sina"
    for item in db.fetch_many(sql, 10):
        print(item)
    return "hello"

