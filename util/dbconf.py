# -*- coding: utf-8 -*-

import configparser

filename = r'moenv.conf'
env = "active"

cf = configparser.ConfigParser()
cf.read(filename, encoding='utf-8')

MYSQL_HOST =cf.get(env, "MYSQL_HOST")
MYSQL_USER = cf.get(env, "MYSQL_USER")
MYSQL_PW = cf.get(env, "MYSQL_PW")
MYSQL_DB =  cf.get(env, "MYSQL_DB")
MYSQL_PORT =  cf.getint(env, "MYSQL_PORT")

#REDIS_HOST = cf.get(env, "REDIS_HOST")
#REDIS_PORT = cf.get(env, "REDIS_PORT")
#REDIS_PWD = cf.get(env, "REDIS_PWD")
#REDIS_CELERYDB = cf.get(env, "REDIS_CELERYDB")
#REDIS_FLOWDB =cf.get(env, "REDIS_FLOWDB")

#NEO4J_HOST = cf.get(env, "NEO4J_HOST")
#NEO4J_USER = cf.get(env, "NEO4J_USER")
#NEO4J_PW = cf.get(env, "NEO4J_PW")
#NEO4J_HTTPPORT = cf.getint(env, "NEO4J_HTTPPORT")
#NEO4J_HTTPBOLT = cf.getint(env, "NEO4J_HTTPBOLT")

#KAFKA_SERVERS = eval(cf.get(env, "KAFKA_SERVERS"))
#KAFKA_USER = cf.get(env, "KAFKA_USER")
#KAFKA_PASSWORD =cf.get(env, "KAFKA_PASSWORD")
#TOPIC_NAME=cf.get(env, "TOPIC_NAME")
#CONSUMER_ID=cf.get(env, "CONSUMER_ID")