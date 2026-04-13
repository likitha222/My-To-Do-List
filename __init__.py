from flask import Flask, render_template, url_for, request ,redirect
import random

app=Flask(__name__)

todos=[
    {
        'id':1,
        'name':'clean my room',
        'checked':False ,
    },
    {
        'id':2,
        'name':'get a job',
        'checked':False,
    },
]


@app.route("/",methods=["GET","POST"]) 
@app.route("/home",methods=["GET","POST"])
def home():
    if(request.method=="POST"):
        todo_name=(request.form["to-do_name"])
        curr_id=random.randint(1,1000)
        todos.append({        
            'id':curr_id,
            'name':todo_name,
            'checked':False,
        })
    return render_template("index.html", items=todos)

@app.route("/checked/<int:todo_id>",methods=["POST"])
def checked_todo(todo_id):
    for todo in todos:
        if todo['id']==todo_id:
            todo['checked']=not todo["checked"]
            break 
    return redirect(url_for("home"))
    

@app.route("/delete/<int:todo_id>",methods=["POST"])
def delete_todo(todo_id):
    global todos
    for todo in todos:
        if todo['id']==todo_id:
            todos.remove(todo)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)