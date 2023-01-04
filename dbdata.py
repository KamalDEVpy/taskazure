from flask import request
from flask import jsonify, json
from passerby_file import *
import sqlite3 as sql



#### CREATE RECORD ####
def create_record(input_data,schema_name):
    dbname = '{}.db'.format(schema_name)
    # print('++++++++++++____________+++++++++',schema_name)
    
    con=sql.connect(dbname)
    cur=con.cursor()

    json_datas = request.get_json()
    create_func(json_datas)
    print("--<<<<<<<<<<>>>>>>>>>>>>--",json_datas)

    model = request.json['model']
    if model == "":
        return("Model Name Should not be empty")
        
    qty = request.json['qty']
    price = request.json['price']
    print("TYPE*****--------->>>>>>>>>>>>>>>.",type(price))
    tab_data = "INSERT INTO {} (MODEL,QTY,PRICE) values (?,?,?)".format(schema_name)
    print("****************",tab_data)
    cur.execute(tab_data,(model,qty,price))
    # print("****************",p)
    con.commit()
    return ('Successfully added to',schema_name)


#### DELETE RECORD ####
def delete_record(input_data,schema_name):
    dbname = '{}.db'.format(schema_name)
    query = "delete from {} where".format(schema_name)
    # print('++++++++++++____________+++++++++',schema_name)
    con=sql.connect(dbname)
    cur=con.cursor()

    json_datas = request.get_json()
    del_upd_ret_func(json_datas)

    data  = request.get_json()
    data = json.dumps(data)
    data = json.loads(data)

    uid = data['uid']
    qty = data['qty']
    price = data['price']
    model = data['model']
    
    try:
        cur.execute("delete from {} where uid={}".format(schema_name,uid))
        con.commit()

        return('Successfully deleted from',schema_name)

    except:
        for values in data:
            if ((model=="") and (price=="") and (qty)==""):
                return("No data given")
            elif data[values]=="" or values=="appid" or values=="action":
                pass
            else:
                query = query+" {}={} and".format(values,data[values])
        query = query.rsplit(' ', 1)[0]
        print("******************",query)

        try:
            cur.execute("{}".format(query))
            con.commit()
            return('Successfully deleted from',schema_name)
        except:
            return("Something went wrong")


#### UPDATE RECORD ####
def update_record(input_data,schema_name):
    dbname = '{}.db'.format(schema_name)
    con=sql.connect(dbname)
    cur=con.cursor()

    json_datas = request.get_json()
    del_upd_ret_func(json_datas)

    model=request.json['model']
    qty=request.json['qty']
    price=request.json['price']
    uid=request.json['uid']

    if uid=="" or model=="":
        return("Something went wrong...")

    
    tab_data = "update {} set model=?, QTY=?, PRICE=? where UID=?".format(schema_name)
    cur.execute(tab_data,(model,qty,price,uid))
    con.commit()
    return('Successufully updated for table',schema_name)


#### READ RECORD ####
def read_record(input_data,schema_name):

    json_datas = request.get_json()
    del_upd_ret_func(json_datas)

    datas = []   #for output showing
    dbname = '{}.db'.format(schema_name)
    query = "select * from {} where ".format(schema_name)
    print('++++++++++++____________+++++++++',schema_name)


    data  = request.get_json()
    data = json.dumps(data)
    data = json.loads(data)

    for values in data:
        if data[values]=="" or values=="appid" or values=="action":
            pass
        else:
            query = query+"{}={} and ".format(values,data[values])
    query = query.rsplit(' ', 2)[0]
    print("++++++++++*******+++++++++*************",query)

    con=sql.connect(dbname)
    con.row_factory=sql.Row
    cur=con.cursor()
    try:
        cur.execute("{}".format(query))
        rows = cur.fetchall()
        print("T%%TT%T%T%T%T%T%",rows)
        for row in rows:
            print("Y^Y^Y^Y^Y^Y^",row)
            datas.append([x for x in row])
        if datas == []:
            return("No data's Found")
        else:
            for i in datas:
                return("Date as of your query mentioned",i)
    except:
        return("Something went wrong")
