from flask import Flask,jsonify,request

app=Flask(__name__)

contacts=[{'id':1,'name':'Rahul','Age':'35','done':False},
         {'id':2,'name':'Scarlet','Age':'24','done':False}]

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json: 
        return jsonify({ "status":"error", "message": "Please provide the data!" },400)
    task = { 'id': tasks[-1]['id'] + 1, 'name': request.json['name'], 
        'Age': request.json.get('Age', ""), 'done': False }
    tasks.append(task)
    return jsonify({ "status":"success", "message": "Task added succesfully!" })

if (__name__ == "__main__"): 
    app.run(debug=True)