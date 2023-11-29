from flask import jsonify         #jsonify :convert disctionary into module object

def create_response(data,error=None):
    #create empty dictionary
    d= dict()

    if(error==None):
        d={
            "status":"success",
            "data":data
        }
    else:
        d={
            "status":"failure"
        }

    return d    
