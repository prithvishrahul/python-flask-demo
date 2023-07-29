from flask import Flask, render_template

app=Flask(__name__)

Cities=[
    {
    'id':1,
    'name':"India"
    },
    {
    'id':2,
    'name':"SriLanKa"
    },
    {
    'id':1,
    'name':"USA"
    },
    {
    'id':1,
    'name':"China"
    }
]

@app.route("/")
def hello_rahul():
    print(takewebcode())
    return render_template('Index.html',cities=Cities)


def takewebcode():
     s=render_template('Index.html',cities=Cities)
     return s
    
app.run(host="0.0.0.0",debug=True)