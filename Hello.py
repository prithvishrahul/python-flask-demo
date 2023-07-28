from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_rahul():
    return "<h1>Hello Rahul</h1>"

app.run(host="0.0.0.0",debug=True)