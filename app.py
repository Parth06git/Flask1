from datetime import datetime
from turtle import title
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2000), nullable=False)
    desc = db.Column(db.String(2000), nullable=False)
    dea = db.Column(db.String(2000), nullable=False)

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.title}"


@app.route('/', methods=['GET', "POST"])
def hello_world():
    if request.method == "POST":
        title=request.form['title']
        desc = request.form['desc']
        dea = request.form['dea']
        todo = Todo(title=title, desc=desc, dea=dea)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)


@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template('about.html')

@app.route('/delete/<int:Sno>')
def delete(Sno):
    todo = Todo.query.filter_by(Sno=Sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/update/<int:Sno>', methods=['GET', "POST"])
def Update(Sno):
    if request.method=='POST':
        title=request.form['title']
        desc = request.form['desc']
        dea = request.form['dea']
        todo = Todo.query.filter_by(Sno=Sno).first()
        todo.title = title
        todo.desc = desc
        todo.dea = dea
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo = Todo.query.filter_by(Sno=Sno).first()
    return render_template('update.html', todo = todo)


