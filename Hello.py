from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello_rahul():
    return render_template('Index.html')

app.run(host="0.0.0.0",debug=True)