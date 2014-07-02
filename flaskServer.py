#-*- coding: utf-8 -*-
from flask import Flask, render_template, make_response, session, redirect, url_for, escape, request,jsonify,Response   
import pymongo, __builtin__, datetime, string
from dateutil import parser
import time as T, json # json.dumps
#import MySQLdb, cPickle, numpy as n

from maccess import mdc as U
U=U.u1
HTAG="#cibervoto"
HTAG_=HTAG.replace("#","NEW")

app = Flask(__name__)

@app.route("/")
def hello():
    client=pymongo.MongoClient(U)
    db = client[U.split("/")[-1]]
    C = db[HTAG_] #collection
    msgs=[i for i in C.find()]
    info=[(mm["user"]["screen_name"],mm["text"],mm["created_at"]) for mm in msgs]
    text_block=string.join([str(ii) for ii in info],"<br />")
    return text_block

@app.route("/votos/")
def votos():
    client=pymongo.MongoClient(U)
    db = client[U.split("/")[-1]]
    C = db[HTAG_] #collection
    msgs=[i for i in C.find()]
    consultas={}
    for msg in msgs:
        msg_=msg["text"].split(" ")
        if msg_[2] in ("+1","-1","0"):
            # voto
            consulta=msg_[1]
            if consulta in consultas.keys():
                consultas[consulta][msg_[2]]+=1
            else:
                consultas[consulta]={}
                consultas[consulta]["+1"]=0
                consultas[consulta]["-1"]=0
                consultas[consulta]["0"]=0
                consultas[consulta][msg_[2]]+=1
    return str(consultas)
    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
