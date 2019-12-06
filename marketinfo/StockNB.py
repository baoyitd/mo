'''
Created on 2019年12月2日

@author: baoyi
'''

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from marketinfo.db import get_db
from marketinfo.BaseResponse import dataResp, dataRespSuc
from flask_cors import CORS

bp = Blueprint('stocknb', __name__, url_prefix='/stock')
CORS(bp) 

@bp.route("/nb")
def getStcokNB():
    #return "hello world"
    db = get_db()
    sql = "select bk,code,name,rname,rurl from t_stockreport_sina where isuseful = 1 order by rname desc"
    al = db.fetch_many(sql,200)
    #print(al)
    return dataResp(al)

@bp.route('/<int:code>/tags', methods=['POST'])
def setTags(code):
    tags = request.get_json()
    print(code,tags)
    '''
    if (tags is None)  or (tags.get("tags") is None):
        return dataRespSuc("参数有误", None)
    else:
    '''
        
    
    
