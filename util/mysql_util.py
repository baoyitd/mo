'''
Created on 2017年5月19日

@author: baoyi
'''
# -*- coding: utf-8 -*-

'''
    默认读取eve库，解决pymysql查询自动带库名不能查询eve数据库问题
    MySQL的处理库
    解决两个问题：1.连接池；2.公共insert/update/query接口
'''

import pymysql
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
from DBUtils.PersistentDB import PersistentDB
from util import dbconf

sql_settings = {'mysql': {'host': dbconf.MYSQL_HOST, 'port': dbconf.MYSQL_PORT, 'user': dbconf.MYSQL_USER, 'passwd': dbconf.MYSQL_PW, 'db': dbconf.MYSQL_DB, 'charset':'utf8'}}

class MySqlUtil(object):
    __pool = {}
    __con = None
    _con = None
    _cursor = None
    
    def __init__(self,conf_name='mysql', pooled=False):
        self._con = MySqlUtil.__get_conn(conf_name, pooled)
        self._cursor = self._con.cursor()
        
    def __del__(self):
        self.close()

    @classmethod
    def __get_conn(cls, conf_name='mysql', pooled=False):
        if pooled:
            if conf_name not in MySqlUtil.__pool:
            #print 'create pool for %s' % conf_name
                MySqlUtil.__pool[conf_name] = PooledDB(creator=pymysql,
                                                       mincached=1, maxcached=20,
                                                       use_unicode=True, 
                                                       cursorclass=DictCursor,
                                                       **sql_settings[conf_name])
            return MySqlUtil.__pool[conf_name].connection()
        else:
            if MySqlUtil.__con == None:
                MySqlUtil.__con = PersistentDB(pymysql,cursorclass=DictCursor,**sql_settings[conf_name]).connection()
            return MySqlUtil.__con
            

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._con:
            self._con.close()

    # insert
    def insert_one(self, sql, value):
        return self._cursor.execute(sql, value)

    def insert_many(self, sql, values):
        return self._cursor.executemany(sql, values)

    # update
    def update(self, sql, param=None):
        return self._cursor.execute(sql, param)

    # query
    def fetch_all(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def fetch_one(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def fetch_many(self, sql, num, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result
    
    def commit(self):
        self._con.commit()

