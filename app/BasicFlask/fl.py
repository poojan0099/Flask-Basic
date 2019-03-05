from flask import Flask
app=Flask(__name__)

@app.route("/https://www.amazon.in/?ie=UTF8&tag=googinabkkenshoo-21&ascsubtag=_k_EAIaIQobChMIkfCIpZre4AIVkB0rCh1T3g5-EAAYASAAEgKSVvD_BwE_k_&gclid=EAIaIQobChMIkfCIpZre4AIVkB0rCh1T3g5-EAAYASAAEgKSVvD_BwE")
def index():
    return "Hello world"

if __name__=="__main__":
    app.run()
