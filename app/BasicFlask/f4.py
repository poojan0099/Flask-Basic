from flask import Flask,render_template
app=Flask(__name__)

@app.route("/about")
def index():
    return "Hello world"

@app.route("/bot")
def kai():
    return render_template(tmp.html)

if __name__=="__main__":
    app.run()
