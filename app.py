from flask import Flask,request
from flask import json, jsonify
# from files.data_handling import *
# from files.tes_1 import *
from dbdata import *
app=Flask(__name__)


@app.route('/')
def home():
    return ('Dynamic DB')

@app.route("/test/", methods=["GET", "POST", "PUT", "DELETE"])
def receive_request():
    input_data = request.get_json()
    # print("input_data", input_data)
    if input_data["appid"]=="DATABASE1":
        schema_name="DATABASE1"
        print ("===============",schema_name)
    if input_data["appid"]=="DATABASE2":
        schema_name="DATABASE2"

    

    if input_data["action"] == "cre":
        print ("===============",schema_name)
        return (json.dumps(create_record(input_data,schema_name)))    
        
    if input_data["action"] == "del":
        print ("===============",schema_name)
        return (json.dumps(delete_record(input_data,schema_name)))   

    if input_data["action"] == "ret":
        print ("===============",schema_name)
        return (json.dumps(read_record(input_data,schema_name)))

    if input_data["action"] == "upd":
        print ("===============",schema_name)
        return (json.dumps(update_record(input_data,schema_name)))  
    
        



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)