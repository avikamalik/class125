from flask import Flask,jsonify,request
api=Flask(__name__)
@api.route("/")
def hello():
    return "hi"

tasks=[
    {
        "id":1,
        "title":"complete homework",
        "done":False
    },
     {
        "id":2,
        "title":"do laundry",
        "done":True
    },
    
]

@api.route("/getdata")
def getdata():
    return jsonify({"data":tasks})

@api.route("/addtask",methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({"message":"please enter some information"})
    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "done": request.json["done"]
    },
    tasks.append(task)
    return jsonify({"message":"task added succesfully"})

api.run()