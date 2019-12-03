'''
Created on 2019年12月2日

@author: baoyi
'''

from util.mysql_util import MySqlUtil

from flask import g

def get_db():
    if 'db' not in g:
        g.db = MySqlUtil()
    return g.db

def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()