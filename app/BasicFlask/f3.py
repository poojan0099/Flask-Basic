from flask import Flask
app=Flask(__name__)

@app.route("/about")
def index():
    return "Hello world"

@app.route("/bot/<name>")
def kai(name):
    return "hello! "+name

if __name__=="__main__":
    app.run()
